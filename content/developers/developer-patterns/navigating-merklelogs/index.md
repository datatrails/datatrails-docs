---
 title: "Navigating the Merkle Log"
 description: "Describes the serialization format of the DataTrails verifiable data structure"
 lead: "Accessing the data needed to verify from first principals"
 draft: false
 images: []
 menu:
   developers:
     parent: "developer-patterns"
 weight: 40
 toc: true
 aliases:
  - /docs/beyond-the-basics/navigating-merklelogs/
---

This article explains how to navigate the Merkle Log, using the DataTrails Merkle Mountain Range implementation.

DataTrails publishes the data necessary for immediately verifying events to highly available commodity cloud storage.
"Verifiable data" is synonymous with *log* or *transparency log*.
Once verifiable data is written to the log it is never changed.
The log only grows, it never shrinks and data in it never moves within the log.

To work with Merkle Log format, DataTrails provides [open-source tooling](https://github.com/datatrails/veracity/) for working in offline environments.

To verify DataTrails logs, you will need:

1. A copy of the section of the log containing your event, (or the url to the
   publicly available log data)
1. A copy of any log *seal* from *any* time after your event was included
1. A copy of any events you wish to verify are included within the log
1. A Tenant ID to run the samples

For reference:

- DataTrails log implementation: [go-datatrails-merklelog](https://github.com/datatrails/go-datatrails-merklelog).
- Examples for verification: [go-datatrails-demos](https://github.com/datatrails/go-datatrails-demos/)
- Log inclusion and introspection: [veracity](https://github.com/datatrails/veracity/blob/main/README.md)

To reproduce these examples from first principals, using only the raw verifiable data structure, an understanding of the log format is provided by this article.

If you already know the basics, and want a straight forward way to deal with the dynamically sized portions of the format, please see [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables)

## Environment Configuration

DataTrails operates customer specific Tenants, and a single public tenant.

- **Public events** are shared on the DataTrails public tenant.

- **Protected events** are only visible to the tenant owner, but the commitment (hash) in the log is public.

The examples in this article use a DataTrail's Synsation demo tenant's to represent protected events.

To view *your* protected events, replace `TENANT` with your `Tenant ID`.

Within the [DataTrails app](https://app.datatrails.ai), click the top/right corner, selecting copy Tenancy Identity.
{{< img src="CopyTenancyIdentity.png" alt="Rectangle" caption="<em>Copy Tenant ID</em>" class="border-0" >}}

Update the variables to fit your environment:

```bash
# DataTrails Public Tenant
export PUBLIC_TENANT="6ea5cd00-c711-3649-6914-7b125928bbb4"

# Synsation Demo Tenant
# Replace to view your Tenant logs ane events
export TENANT="6a009b40-eb55-4159-81f0-69024f89f53c"
```

## Each Log Is Comprised of Many Massif Blobs, Each Containing a Fixed Number of Leaves

```output
+-----------+ +-----------+ .. +----------+
| massif 0  | | massif 1  |    | massif n
+-----------+ +-----------+ .. +----------+
```

> Illustration demonstrating the last massif is always in the process of being *appended* to

What is a massif?
In this context, a massif means a [group of mountains that form a large mass](https://www.oxfordlearnersdictionaries.com/definition/american_english/massif).
Massif originates from the verifiable data structure used in the Merkle Mountain Range [^1] (MMR) based log.

[^1]: Merkle Mountain Ranges have seen extensive use in systems that need long term tamper evident storage, notably [zcash](https://zips.z.cash/zip-0221), [mimblewimble](https://github.com/mimblewimble/grin/blob/master/doc/mmr.md), and [many others](https://zips.z.cash/zip-0221#additional-reading).

Merkle Mountain Ranges are attributed to [Peter Todd](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-May/012715.html), though much parallel invention has occurred.
The "post order", write once & append only nature of the tree organization was first discussed in 3.3 of the [Crosby, Wallach paper](https://static.usenix.org/event/sec09/tech/full_papers/crosby.pdf).
They have been independently analyzed in the context of [cryptographic asynchronous accumulators](https://eprint.iacr.org/2015/718.pdf), Generalized multi-proofs for [Binary Numeral Trees](https://eprint.iacr.org/2021/038.pdf).
And also by the [ethereum research community](https://ethresear.ch/t/batching-and-cyclic-partitioning-of-logs/536).

Each massif contains the verifiable data for a fixed number, and sequential range, of events.
The number of events is determined by the log configuration parameter `massif height`.
Within DataTrails, all logs currently have a massif height of `14`, and the number of event *leaf* log entries in each massif is 2<sup>height-1</sup>, which is 2<sup>14-1</sup> leaves, which is `8192` leaves.
`14` was chosen as it affords a massif storage size of comfortably under 4mb (less than 2 actually), and for many situations it is practical to handle this size as "one lump".
See [reconfiguration](#the-massif-height-is-constant-for-all-blobs-in-a-log-configuration) for more info.

[Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) provides a shortcut for picking the right massif.
It can also be fairly easily computed from only the `merklelog_entry.commit.index` *mmrIndex* on the event using the [example javascript](/developers/developer-patterns/massif-blob-offset-tables#the-algorithms-backing-the-table-generation).

## Every Massif Blob Is a Series of 32 Byte Aligned Fields

Every massif in a log is structured as a series of `32` byte fields.
All individual entries in the log are either 32 bytes or a small multiple of `32`.

```output
  0               32
  +----------------+
  |                | field 0
  +----------------+
  .                .
  .                .
  +----------------+
  |                | field n
  +----------------+
```

Recalling our configuration (above), the tenants first massif blob can be found at:

{{< tabs >}}
   {{< tab name="bash" >}}

  ```bash
  curl https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/$TENANT/0/massifs/0000000000000000.log -o 0.log
  ```

  {{< /tab >}}
{{< /tabs >}}

Each massif is stored in a numbered file.
The filename (`0000000000000000.log`) is the 16-character, zero-padded, massif index.

The DataTrails attestation for each massif can be found at a closely associated url.

For the massif above it is:  
{{< tabs >}}
   {{< tab name="bash" >}}

  ```bash
  curl https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/$TENANT/0/massifseals/0000000000000000.sth -o 0.sth
  ```

  {{< /tab >}}
{{< /tabs >}}

This is a simple reverse proxy to the native azure blob store where your logs are store.
The full [Azure REST API](https://learn.microsoft.com/en-us/rest/api/azure/) provides getting specific massif blobs.
For reasons of cost, all operations are subject to rate limits, listing blobs is not possible, though filtering blobs by tags is permitted.
Both the massif blobs and the log seal blobs are always tagged with the most recent idtimestamp for the log.
In the case of the masssif blobs, it is the idtimestamp most recently added to the log. In the case of the seal blob it is the most recent log entry that has been attested by DataTrails. The tag name is `lastid`

## Re-Creating Inclusion Proofs Requires Only One Massif

The variable section of the massif blob is further split into the *accumulator* for the preceding log state followed by the regular massif nodes:

```output
+----------------+----------------+
| FIXED          | HEADER DATA    |
|                +----------------+  fixed size
|        SIZE    | TRIE-DATA      |  pre-filled with zeros, populated as leaves are added
+----------------+----------------+
| VARIABLE       | PEAK           |  accumulator succinctly committing the entire preceding log state,
|                |         STACK  |    which is write once on massif create
|   write once   +----------------+
|                | MMR            | grows until 2^(height-1) leaves are added
.                .   NODES        |
.   APPEND ONLY  .                |
+----------------+----------------+
```

The accumulator is more precisely a cryptographic, asynchronous, accumulator whose properties are formally defined in this [paper](https://eprint.iacr.org/2015/718.pdf).
We refer to it as the peak stack due to how we maintain it and the fact that it is composed exclusively of "peak" nodes taken from the preceding log.

DataTrails provides convenience look up tables for [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables), and implementations of the algorithms needed to produce those tables in many languages under an MIT license.

## The First 32 Byte Field in Every Massif Is the Sequencing Header

The following curl command reads the version and format information from the header field `0`

{{< tabs >}}
   {{< tab name="bash" >}}

  ```bash
  curl -s \
    -H "Range: bytes=0-31" \
    -H "x-ms-blob-type: BlockBlob" \
    -H "x-ms-version: 2019-12-12" \
    https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/$TENANT/0/massifs/0000000000000000.log \
    | od -An -tx1 \
    | tr -d ' \n'
  ```

  generates a version information, similar to:

  ```output
  00000000000000009148fda07f06640000000000000000000000010e00000000
  ```

  {{< /tab >}}
{{< /tabs >}}

{{< note >}}The request requires no authentication or authorization.{{< /note >}}

The structure of the header field is:

```output
| type| idtimestamp| reserved |  version | epoch  |massif height| massif i |
| 0   | 8        15|          |  21 - 22 | 23   26|27         27| 28 -  31 | start and end byte indices, closed range
| 1   |     8      |          |      2   |    4   |      1      |     4    | count of bytes
```

The `idtimestamp` of the last leaf entry added to the log is always set in the header field.

In the hex data above, the `idtimestamp` of the last entry in the log is `9148fcc832066400`[^2], the version is `0`, the timestamp epoch is `1`, the massif height is `14`, and the massif index is `0`.

[^2]: The `idtimestamp` value is 64 bits, of which the first 40 bits are a millisecond precision time value and the remainder is data used to guarantee uniqueness of the timestamp.
DataTrails uses a variant of the [Snowflake ID](https://en.wikipedia.org/wiki/Snowflake_ID) scheme.
The DataTrails implementation can be found at [nextid.go](https://github.com/datatrails/go-datatrails-merklelog/blob/main/massifs/snowflakeid/nextid.go#L118)

### Decoding an idtimestamp

The `idtimestamp` is 40 bits of time at millisecond precision.
The `idtimestamp` in the header field is always set to the `idtimestamp` of the most recently added leaf.

The following examples depend on a python environment:

{{< tabs >}}
  {{< tab name="Python" >}}

  ```python
  import datetime
  import sys

  def idtimestamp_to_date(id: str):
      """Safely convert an idtimestamp hex string to a regular date time"""
      
      # ignore the common '0x' prefix
      if (id.startswith("0x")):
          id = id[2:]
      
      if len(id) > 18:
          raise ValueError("idtimestamp must be 18 or 16 hex chars")
      epoch = 1 # the epochs are aligned with the unix epoch but are half as long
      if len(id) == 18:
          epoch = int(id[:2])
          id = id[2:]
      
      if len(id) != 16:
          raise ValueError("idtimestamp must be 18 or 16 hex chars")
      
      # To get the time portion we strip the trailing sequence and generator id
      unixms=int((
          bytes.fromhex(id)[:-3]).hex(), base=16
          ) + epoch*((2**40)-1)
      return datetime.datetime.fromtimestamp(unixms/1000)

  print(idtimestamp_to_date('9148fcc832066400'))
  ```

  Generates:

  ```output
  2024-08-13 00:46:51.569000
  ```

  {{< /tab >}}
{{< /tabs >}}

In this example, the last entry in the log (at that time) was `2024/08/13`, a little before 1am UTC.

## The trieData entries are 512 bits each and are formed from two fields

With the trie keys, full data recovery can be verified without needing to remember the order that events were added to the log.

Massifs can be recovered independently even if the data for other massifs is incomplete.

The index also provides for proof of exclusion. Proof that a specific event is not in the index.
As the event identities contribute to both the index keys and the leaf entries,
and as the keys are time ordered on addition, it is possible to audit the specific range.
This will confirm the log is consistent with the index for the time range in which the disputed item is claimed to exist.

The trieData section is 2 \* 32 \* 2<sup>height</sup> bytes long, which is exactly double what is needed.
For a standard massif height of 14, it has 8,192 entries in the first 524,288 bytes.
The subsequent 524,288 will always be zero.
The format of each entry is then, for a massif height of 14:

```output
+----------------+
| HEADER DATA    |
+----------------+

288
+----------------+
| TRIE-DATA      |
|                |
|                |
|................| 288 + 524288 = 524576
|  always        |
|                |
|       zero     |
+----------------+ 288 + 524288 * 2 = 1048864
```

Each entry is formatted like this

```output
0                                                        31
SHA256(BYTE(0x00) || tenant-identity || event.identity)
0                                       BYTES(IDTIMESTAMP)
32                                      56               63
```

Described in further detail in the [term-cheatsheet](https://github.com/datatrails/go-datatrails-merklelog/blob/main/term-cheatsheet.md#trie-entry)
Note that the `idtimestamp` is unique to the tenant and the DataTrails service.
When sharing events with other tenants, the `idtimestamp` will not correlate directly with activity in other tenant logs.

When a massif is initialized the trieData is pre-populated for all leaves and set to all zero bytes.
As events are recorded in the log, the zero-padded index is filled in.
A sub-range of field 0 will change when saving the last `idtimestamp` in it.
The MMR node values are strictly only ever appended to the blob.
Once appended they will never change and they will never move.

Returning to the trieData section, given an event identity of:

`assets/20d6f57c-bce2-4be9-8e70-95ded25399b7/events/bbd934cb-a20f-44c9-aa5d-a3ce333c5208`

The trieKey for the synsation tenant's log is:
`d273400cca0d594ddbd4f04bc9275e0e6d995da1accafa00b5be879a265ecda9`

The following python snippet generates a trieKey from the event data to confirm what should be in the index at a specific position.

{{< tabs >}}
   {{< tab name="Python" >}}

  ```python
  import hashlib
  import os

  TENANT=os.environ['TENANT']
  PUBLIC_TENANT=os.environ['PUBLIC_TENANT']
  ASSET='20d6f57c-bce2-4be9-8e70-95ded25399b7'
  EVENT='bbd934cb-a20f-44c9-aa5d-a3ce333c5208'

  def triekey(tenant, event):
      h = hashlib.sha256()
      h.update(bytes([0]))
      h.update(tenant.encode())
      h.update(event.encode())
      return h.hexdigest()

  print(triekey(
  "tenant/" + TENANT,
  "assets/" + ASSET + "/events/" + EVENT))
  ```

  generates:

  ```output
  d273400cca0d594ddbd4f04bc9275e0e6d995da1accafa00b5be879a265ecda9
  ```

  {{< /tab >}}
{{< /tabs >}}

The above example is an event on a public asset, so it can be found in the public tenant's merkle log.

Using the python requests object (or curl), fetch the public tenants log,

{{< tabs >}}
   {{< tab name="Python" >}}

  ```python
  import requests
  import os

  TENANT=os.environ['TENANT']
  
  r = requests.get('https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/'+
    TENANT+'/0/massifs/0000000000000000.log',
    headers={"x-ms-blob-type": "BlockBlob", "x-ms-version": "2019-12-12"})
  
  with open("mmr.log", "w") as f:
    f.write(r.text)
  ```

  {{< /tab >}}
  {{< tab name="Bash" >}}

  ```bash
  curl -s \
    -H "x-ms-blob-type: BlockBlob" \
    -H "x-ms-version: 2019-12-12" \
    https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/$TENANT/0/massifs/0000000000000000.log -o mmr.log
  ```

  {{< /tab >}}
{{< /tabs >}}

Using python, we can more readily illustrate the 32 byte aligned format.

{{< tabs >}}
   {{< tab name="Python" >}}

  ```python
  import requests
  import binascii
  import sys
  SYNSATION_TENANT = "6a009b40-eb55-4159-81f0-69024f89f53c"
  TENANT=os.environ.get('TENANT', SYNSATION_TENANT) # default to synsation if not in env 
  
  def readfields(tenant, log="0000000000000000"):
      r = requests.get('https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/'+tenant+'/0/massifs/'+log+'.log')
      hex = binascii.hexlify(r.content).decode('utf-8')
      for i in range(int(len(hex) / 64)):
          yield hex[i*64:(i+1)*64]
  
  log = "0000000000000000"
  for field in readfields(TENANT, log):
      print(field)
  ```

  The first few fields will look like

  ```output
  00000000000000009148fda07f06640000000000000000000000010e00000000
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  d273400cca0d594ddbd4f04bc9275e0e6d995da1accafa00b5be879a265ecda9
  0000000000000000000000000000000000000000000000009148fcc832066400
  f67192c6a4fe6a3454000225647deb37e7c488461b1d52f8d1dc58222d49d4db
  0000000000000000000000000000000000000000000000009148fccedb045d00
  1057b8d9caaf1f09e46e04a4e36295276fa8f2ef676144f4b90fc47e335ea51e
  0000000000000000000000000000000000000000000000009148fd0d47066400
  7fe0c5553a639bbeb5e0c26e24c94722f126fa258560097c531e9eb12e12dc88
  0000000000000000000000000000000000000000000000009148fd52e7066400
  0e561df1aa165967ffe12b0d84491e29349d0022f840d9dcb5bb3fe62551ef5c
  0000000000000000000000000000000000000000000000009148fda07f066400
  0000000000000000000000000000000000000000000000000000000000000000
  0000000000000000000000000000000000000000000000000000000000000000
  ```

  {{< /tab >}}
{{< /tabs >}}

Note the trieKey we derived earlier is easily spotted at row 9, and its
`idtimestamp`, `9148fcc832066400`, is in the subsequent field

All public events are automatically shared to the public tenant. This makes the
event data visible without access control. The example event we created in the
Synsation tenant is a public event. We can obtain its corresponding entry in the
log by deriving its trieKey, and recalling our implementation for `triekey` above

Obtain the trie key for the public tenant event:

{{< tabs >}}
   {{< tab name="Python" >}}

  ```python
  import hashlib
  import os
  
  TENANT=os.environ['TENANT']
  PUBLIC_TENANT=os.environ['PUBLIC_TENANT']
  ASSET='20d6f57c-bce2-4be9-8e70-95ded25399b7'
  EVENT='bbd934cb-a20f-44c9-aa5d-a3ce333c5208'
  
  def triekey(tenant, event):
      h = hashlib.sha256()
      h.update(bytes([0]))
      h.update(tenant.encode())
      h.update(event.encode())
      return h.hexdigest()
  
  print(triekey(
    "tenant/" + PUBLIC_TENANT,
    "assets/" + ASSET +
    "/events/" + EVENT))
  ```

  Generates:

  ```output
  c31114a64b9dca1376d7af999d35b4fa05a75965cb49d2b58386e19b8bbc73a9
  ```

  {{< /tab >}}
{{< /tabs >}}

If you similarly run `getlog` (from the example above) on the public tenant, the public trieKey is found
at line 2390.  As this log commits events shared from many tenants, the MMRIndex
of the publicly committed event is different (and quite a lot higher)

The full details of the publicly available event can be found [here](https://app.datatrails.ai/merklelogentry/20d6f57c-bce2-4be9-8e70-95ded25399b7/bbd934cb-a20f-44c9-aa5d-a3ce333c5208?public=true)

Noting that the `public` routing prefix is not prepended on the event identity.

This works the same for regular OBAC shares, a shared event is committed both to
the originating tenants log and to the recipient tenants log.

It is not possible to directly correlate activity between different tenants logs unless you know both the tenant identity and the event identity.
For permissioned events, this will only be available if the executing identity is included in the sharing policy.
The `idtimestamp` is different for each log, guaranteed unique within the context of a single log, and, assuming only good operation of our cloud providers clocks, guaranteed unique system wide.

It is important to remember that timing analysis is possible regardless of whether we have trie keys or not.

## The Peak Stack and MMR Data Sizes Are Computable

See [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) to avoid needing to calculate these.
Implementations of the O(log base 2 n) algorithms are provided in various languages.
They all have very hardware-sympathetic implementations.

## The Massif Height Is Constant for All Blobs in a Log Configuration

For a massif height of `14`, the fixed size portion is `1048864` bytes.

A typical url for a massif storage blob looks like:  
`https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifs/0000000000000000.log`

In the above, the *log configuration* identifier is the `/0/` between the tenant uuid and the `massifs/0000000000000000.log`

The massif height is recorded at the start record of every massif, and guarantees that all massifs in a single configuration path have the same **massif height**.

Currently all DataTrails tenants use the same configuration.
In the future, DataTrails may change the height for massifs.
In a log reconfiguration activity, DataTrails would first publish the tail of the log to the new path. For example: (`/1/massifs/0000000000000123.log`).
The log would be immediately available for continued growth.
The historic configuration continues to be available under the `/0/` path.
Depending on data retention and migration policies for your tenant, the historic configuration can verifiably be migrated to the new path without interrupting service or availability.

This is achieved without impacting the verifiability of the contained data and without invalidating your previously cached copies taken from the earlier massif size configuration.
If reconfigured, a log configuration description will also be published along side the massifs and seals.

Simple binary file compare operations can show that the verifiable data for the new configuration is the same as in the original should you wish to assure yourself of this fact.

The previous configuration path will no longer receive any additions.

{{< note >}}
For the forseeable future (at least months) DataTrails does not anticipate needing to reconfigure the massif height.
{{< /note >}}

## Reading a Specific MMR Node by mmrindex

The variable portion *for the first massif* contains exactly *16383* MMR *nodes*.
Of those nodes, *8192* are the leaf entries in the Merkle tree corresponding to your events.

Given a byte offset in the blob for the start of the MMR data, a query can check for the number of MMR nodes currently in it by doing `(blobSize - mmrDataStart)/32`.

To read a specific MMR node, find the smallest `Last Node` in [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) that is greater than your *mmrIndex* and use that row as your massif index.

Taking the massif index of 0 (row 0) use the first mmrIndex:

{{< tabs >}}
  {{< tab name="Bash" >}}

  ```bash
  LOGSTART=1048864
  MMRINDEX=2376
  curl -s \
    -H "Range: bytes=$(($LOGSTART+$MMRINDEX*32))-$(($LOGSTART+$MMRINDEX*32+31))" \
    -H "x-ms-blob-type: BlockBlob" \
    -H "x-ms-version: 2019-12-12" \
    https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/$PUBLIC_TENANT/0/massifs/0000000000000000.log  \
    | od -An -tx1 \
    | tr -d ' \n'
  ```

  Generates:

  ```output
  3cab877bc730f7e3d652e74b5b9e9a3fad605001c29ebe481764d184c7773f95
  ```

  {{< /tab >}}
{{< /tabs >}}

You can confirm this on the merklelog [page](https://app.datatrails.ai/merklelogentry/20d6f57c-bce2-4be9-8e70-95ded25399b7/861dd529-3616-4ad2-b2a9-702da77b8588?public=true) in the public tenant for this event. Look for the "Merkle Leaf" field.

Optionally use [veracity](https://github.com/datatrails/veracity/) to confirm:

{{< tabs >}}
   {{< tab name="bash" >}}

  ```bash
  veracity \
  --data-url "https://app.datatrails.ai/verifiabledata" \
  -t tenant/$PUBLIC_TENANT \
  node -i 2376
  ```

  Generates:

  ```output
  3cab877bc730f7e3d652e74b5b9e9a3fad605001c29ebe481764d184c7773f95
  ```

  {{< /tab >}}
{{< /tabs >}}

The example javascript in [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables#the-algorithms-backing-the-table-generation) can be used to accomplish this computationally.

## Leaf Nodes Created by Hashing Event Data

``` output
0                                                        31
SHA256(BYTE(0x00) || BYTES(IDTIMESTAMP) || V3-SCHEMA(event))
```

The V3 Schema defines how the content on your event is consistently converted to bytes prior to hashing.
This works by passing the fields specified in the schema through the [bencode](https://en.wikipedia.org/wiki/Bencode) encoding system.

See our knowledge base [article](https://support.datatrails.ai/hc/en-gb/articles/18120936244370-How-to-independently-verify-Merkle-Log-Events-recorded-on-the-DataTrails-transparency-ledger#h_01HTYDD6ZH0FV2K95D61RQ61ZJ) for an example in javascript and the definition of the V3 fields.

Note that this includes the `event_identity` and `tenant_identity` which are also included in the trieKey hash.

The remaining item is conditioning the `IDTIMESTAMP` for hashing.
If you have the event record from the Events API, the idtimestamp is found at `merklelog_entry.commit.idtimestamp`.
It is a hex string and prefixed with `01` which is the epoch from the header.

To condition the string value, strip the leading `01` and convert the remaining hex to binary.
Then substitute those bytes, in presentation order, for idTimestamp above.

The bytes for the hash are just `bytes.fromhex("019148fccdbf066400"[2:])`

You can use the earlier python example to convert this format to a regular date time.

## Which Nodes

Typically, verifiers would verify the inclusion of an event in the log.
The inclusion is verified by selecting the sibling path needed to recreate the root hash starting from your leaf hash.
Create the leaf hash using the original pre-image data of your event and the *commit* values assigned to it when it was included in the log.

For example:

- The V3 canonical set of fields from your event (as described in our knowledge base [article](https://support.datatrails.ai/hc/en-gb/articles/18120936244370-How-to-independently-verify-Merkle-Log-Events-recorded-on-the-DataTrails-transparency-ledger#h_01HTYDD6ZH0FV2K95D61RQ61ZJ))
- The `merklelog_entry.commit.index` (the mmrIndex of the event in the log)
- The `merklelog_entry.commit.idtimestamp` uniquely placing the record of the log in time (according to our cloud service provider)

Determining the sibling path will be a future article.
First, set the scene by covering how the logical tree nodes map to storage.

What is a sibling path?
To understand this we need to dig into how DataTrails organizes the nodes in the Merkle log in storage and memory.

## Tree Layout in Storage

Merkle trees *prove* things by providing paths of hashes that lead to a single *common root* for all nodes in the tree.
For an MMR, a single root can be produced by "bagging the peaks".
But the list of peaks, from which that single root is produced, is itself precisely determined by the size of the MMR.
Having the peak list is equivalent to having a single root.
And having a path that leads to a peak is equivalent to having a path to a single root
The peak list is an accumulator state and a path to an accumulator is actually more useful.

The formal details, and a very nice visualization of how the peaks combine, is available in this paper on [cryptographic, asynchronous, accumulators](https://eprint.iacr.org/2015/718.pdf) (see Fig 4, page 12)

The peaks are exactly the accumulator described there.

All entries in a Merkle log each have a unique and *short* path of hashes[^3]: , which when hashed together according to the data structures rules, will re-create the same root.
If such a path does not exist, by definition the leaf is not included - it is not in the log.

[^3]: Such a path of hashes is commonly referred to as a "proof", a "witness", and an "authentication path".
A Merkle Tree is sometimes referred to as authenticated data structures or a verifiable data structure. For the purposes of this article, there is no meaningful difference. They are all the same thing. We stick to "verification" and "verifiable data structure" in this article.

Where do those paths come from?
They come from adjacent and ancestor nodes in the hierarchical tree.
This means that when producing the path we need to access nodes throughout the tree to produce the proof.

Using the "canonical" MMR log for illustration, we get this diagram.
The vertical axis is labeled by height index, which is just height - 1.
The connecting diagonal dashes above the "tree line" indicate nodes that belong to one massif but depend on peaks accumulated from earlier massifs.

```output
                          
                       14 
                          \        affectionately called the alpine zone
                6           13             21   
                  \            \              \
    h=2 1 |  2  |  5  |   9  |  12   |  17   | 20  | -- massif 'tree line'
          |     |     |      |       |       |     |
        0 |0   1| 3  4| 7   8|10   11|15   16|18 19|
```

The sibling *proof* path for the leaf with `mmrIndex` `7` would be [`8`, `12`, `6`], and the "peak bagging" algorithm may then be applied to get the root if that was desired.
An inclusion proof against an accumulator entry both equivalent and also more durable, as it is permanently consistent with all future accumulator states.

```output
H(7 || 8) = 9
H(9 || 12) = 13
H(6 || 13) = 14
```

14 is a peak in the MMR. The precise set of peaks are determined exclusively from the current mmr size which is 23 in this case. Showing a leaf has a path to a peak for the MMR is sufficient to prove its inclusion in the MMR.

## Visualizing the “Look Back” Peak Stack

A specific challenge for log implementations with very large data sets is answering "how far back" or "how far forward" may be seen?

MMRs differ from classic binary Merkle trees in how, or even *if*, the incomplete sub-trees are combined into a common root.
For an MMR, the common root is defined by an algorithm for combining the adjacent, incomplete sub-trees.
Rather than by the more traditional, temporary, assignment of un-balanced siblings.
Such un-balanced siblings would later have to be re-assigned (balanced) when there were sufficient leaves to merge the sub-trees.

While a single root can be produced for an MMR, due to the properties of the accumulator construction, there is much less value in doing so.
Typically, verification use cases are better served by paths to an accumulator.

The linear and write once nature of this storage organization is what permits DataTrails to publish the log data immediately after events are added.

The specific properties of Merkle Mountain Ranges lead to an efficiently computable and stable answer to the question of *"Which other nodes do I need"*.
Such that we *know* categorically it is not needed to look *forward* of the current massif and it is precisely known which nodes are needed from the previous massifs.

The "free nodes" in the alpine zone always require "ancestors" from previous nodes when producing inclusion proofs that pass through them, and when adding new nodes to the end of the log.
But those ancestors are precisely the peaks forming the accumulator that attests to the log state and provide efficient, permanently useful, proofs of inclusion and consistency.

The progression of the peak stack (accumulator) can be visualized like this. In this diagram we gather the dependent nodes into the massifs they belong too and carry forward the peak stack (accumulator) that fully authenticates the entire state of the MMR preceding the massif.

```output
      |[]   |[2]  |[6]   |[6,9]  |[14]   |[14,17]| peak stack
      |     |     |      |       |       |       |
      |     |6    |      |13, 14 |       |21     | spurs
      |     |     |      |       |       |       |
h=2 1 |  2  |  5  |   9  |  12   |  17   |  20   | <-- massif height 'tree line'
      |     |     |      |       |       |       |
    0 |0   1 3   4| 7   8|10   11|15   16|18   19|
```

*Note: height is 1 based, height indices are 0 based. So at h=2 we have height index 1.*

The log configuration parameter massif height is the "tree line".
The first leaf addition that causes "break out" is the last leaf of that particular massif.
The "break out nodes" for the last leaf are stored in the same massif as the leaf.
While the leaf count for each massif is fixed, the number of nodes is variable.
The variance is deterministic given only the MMR size.

The look-back nodes are called the *peak stack* because the operations we use to maintain it are stack like.
Entries don't pop off, ever.
Entries just happen to reference it in reverse order of addition when adding new leaves.

The stability of the MMR data comes from the fact that the sub trees are not merged until a right sibling tree of equal height has been produced.
Merging is accomplished by *appending* the new parent immediately after the right sibling.
This means when merged, the sub trees do not change in content or organization, nodes are simply appended to commit them to the log.
This results in the "write-once" and "append only" properties discussed in the [crosby-wallach](https://static.usenix.org/event/sec09/tech/full_papers/crosby.pdf) 3.3 "Storing the log on secondary storage"

## How the Tree Spans the Massifs

A worked example for a Merkle log whose height configuration parameter is set to 2.

### Massif 0

The peak stack size is established for a massif when it is created in its empty state. The size is efficiently calculable from the MMR Index at the start of the new massif. For the first massif the stack will be empty.

When viewed horizontally, we start by denoting the empty stack like this.

```output
++
||
++
```

Then, the leaves for the complete MMR of size 3 from our canonical example are added after the peak stack.

This gives us the final form for massif 0 as:

```output
++---+---+---+
|| 0 | 1 | 2 |
++---+-------+
```

The massif has exactly 3 nodes

The peak stack is empty, and the global tree looks like this:

```output

  1    2  | --- massif tree line massif height index = 1
      / \ |
     0   1| MMR INDICES
     -----|
       0  | MASSIF
```

### Massif 1

Once massif 1 has been constructed, the global tree would be:

```output
2       6       --- max height index = 2
         \
1    2  | 5   | --- massif tree line massif height index = 1
    / \ |/  \ |
   0   1|3   4| MMR INDICES
   -----|-----|
     0  |  1  | MASSIF
```

The layout of massif 1 in storage is

```output
+---++---+---+---+---+
| 2 || 3 | 4 | 5 | 6 |
+---++---+-------+---+
```

For massif `1`, the peak stack is `[2]`.
When node `4` was added, the "back fill nodes" were added to "complete the tree" and were also stored in massif `1`.
The "break out" nodes visually overhang the previous massif, but are stored in massif `1`.

This layout is also known as a "post order" traversal of a binary tree.

Note that the addition of node `6`, while backfilling for `4`, requires node `2` from the previous massif `0`.
This is why it is carried forward in the peak stack.

We can also see that is the *only* node that is required from massif `0` for *any* verification path in massif `1`.

As the log grows, the accumulator (peak stack) moves on.
However, historic verification paths can always be proven to exist in all future accumulators.
Given a pair of signed accumulators that are inconsistent, the broken log is evident.

The key point here is that, in massif `1`, when computing a verification path for nodes `3` or `4`, the only node that is required from massif `0` is available locally in the peak stack (in massif `1`).

This means that should you lose interest in the leaf entries from massif `0`, the whole massif can be deleted without fear that it will impact the verifiability of subsequent items in the log.

If you retain the seal from massif `0`, or if you can count on it being available from another trusted source, you only strictly need to retain leaves of interest and their verification paths.

### Massif 2

The global tree at the end of massif `2`

```output
2       6
          \
1    2  |  5  |  9  |
    / \ |/  \ | / \ |
   0   1|3   4|7   8|
   -----|-----|-----|
     0  |  1  |  2  | MASSIF
```

The layout for massif `2`, showing the peak stack is `[6]`

```output
+---++---+---+---+
| 6 || 7 | 8 | 9 |
+---++---+-------+
```

Note that `6` has replaced `2`.
The `2` is not required for any verification path for elements added in massif `2` or beyond.

### massif 3

The global tree at the end of massif `3`

```output
  3              14
                   \
                    \
                     \
  2        6         13
            \          \
  1    2  |  5  |  9  | 12  |
      / \ |/  \ | / \ | / \ |
     0   1|3   4|7   8|10 11|
     -----|-----|-----|-----|
     | 0  |  1  |  2  |  3  |
     -----|-----|-----|-----|
```

The peak stack is `[6, 9]`. Because both nodes `6` and `9` were needed to complete
the MMR that includes leaf node `11`.

```output
+---+---++----+----+----+----+----+
| 6 | 9 || 10 | 11 | 12 | 13 | 14 |
+---+---++----+----+----+----+----+
```

### Massif 4

The global tree at the end of massif `4`

```output
  3              14
                   \
                    \
                     \
  2        6         13
            \          \
  1    2  |  5  |  9  | 12  |  17  |
      / \ |/  \ | / \ | / \ | /  \ |
     0   1|3   4|7   8|10 11|15  16|
     -----|-----|-----|-----|------|
     | 0  |  1  |  2  |  3  |   4  |
     -----|-----|-----|-----|------|
```

Note that this case is particularly interesting because it completes a full cycle from one perfect power-sized tree to the next.
A fact of the MMR construction is the look back is never further than the most recent 'perfect' tree completing massif.

So the peak stack is `[14]`, discarding `6` and `9`, and the massif `4` layout is:

```output
+---++----+----+----+
| 14|| 15 | 16 | 17 |
+---++----+----+----+
```

## Takeaways

- Merkle logs are divided into massifs, each of which stores verification data for a fixed number of your events.
- Once verification data is written to the log, it never changes.
- The "look back" nodes needed to make each massif self contained are deterministic and are filled in when a new massif is started.
- The dynamically sized portions of the format are all computable, but we offer pre-calculated tables for convenience.
- [Open-source tooling](https://github.com/datatrails/veracity/) exists in multiple languages for navigating the format.
- Given a signed "root", all entries in any copies of your log are irrefutably attested by DataTrails.

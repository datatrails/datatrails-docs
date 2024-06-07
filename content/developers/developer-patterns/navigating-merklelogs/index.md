---
 title: "Navigating the Merkle Log"
 description: "Describes the serialization format of the DataTrails verifiable data structure"
 lead: "Accessing the data needed to verify from first principals"
 draft: false
 images: []
 menu:
   developers:
     parent: "developer-patterns"
 weight: 34
 toc: true
 aliases:
  - /docs/beyond-the-basics/navigating-merklelogs/
---

DataTrails publishes the data necessary for verifying events immediately to publicly readable and highly available commodity cloud storage.  We call this verifiable data your *log* or *transparency log*.

Once verifiable data is written to this log we never change it.  The log only grows, it never shrinks and data in it never moves.

DataTrails provides extensive open-source tooling to work with this format in an offline setting.

To take advantage of this you will need:

1. A copy of the section of the log containing your event (or the url to our
   publicly available log data)
1. A copy of any log *seal* from *any* time after your event was included.
1. A copy of any events you wish to verify (that you retained or that you later retrieved).

The general log implementation is [go-datatrails-merklelog](https://github.com/datatrails/go-datatrails-merklelog). [go-datatrails-demos](https://github.com/datatrails/go-datatrails-demos/) includes examples for different kinds of verification, and [veracity](https://github.com/datatrails/veracity/blob/main/README.md) is a tool for introspecting logs in their native storage.

Should you wish to do this from first principals, using only the raw verifiable data structure, you will additionally need the understanding of the log format offered by this article.

If you already know the basics, and want a straight forward way to deal with the dynamically sized portions of the format, please see [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables)

## Each log is comprised of many massif blobs, each containing a fixed number of leaves

    +----------------+ +----------------+ .. +-----------+
    |     massif 0   | |     massif 1   |    |  massif n
    +----------------+ +----------------+ .. +-----------+

What is a massif?
In this context, it means a [group of mountains that form a large mass](https://www.oxfordlearnersdictionaries.com/definition/american_english/massif).
This term is due to the name of the verifiable data structure used for the log: An MMR or "Merkle Mountain Range" [^1].

[^1]: Merkle Mountain Ranges have seen extensive use in systems that need long term tamper evident storage, notably [zcash](https://zips.z.cash/zip-0221), [mimblewimble](), and [many others](https://zips.z.cash/zip-0221#additional-reading).
Merkle Mountain Ranges are attributed to [Peter Todd](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-May/012715.html), though much parallel invention has occurred. The "post order", write once & append only nature of the tree organisation was first discussed in 3.3 of the [Crosby, Wallach paper](https://static.usenix.org/event/sec09/tech/full_papers/crosby.pdf).
They have been independently analyzed in the context of [cryptographic asynchronous accumulators](https://eprint.iacr.org/2015/718.pdf), Generalized multi-proofs for [Binary Numeral Trees](https://eprint.iacr.org/2021/038.pdf).
And also by the [ethereum research community](https://ethresear.ch/t/batching-and-cyclic-partitioning-of-logs/536).

Each massif contains the verifiable data for a fixed number, and sequential range, of your events.
The number of events is determined by your log configuration parameter `massif height`.

Currently, all logs have a massif height of `14` And the number of event *leaf* log entries in each massif is 2<sup>height-1</sup>, which is 2<sup>14-1</sup> leaves, which is `8192` leaves. 14 was picked because it affords a massif storage size of comfortably under 4mb (less than 2 actually), and for many situations it is practical to handle this size as "one lump". We discuss [reconfiguration here](#the-massif-height-is-constant-for-all-blobs-in-a-log-configuration)


Above, we have drawn `massif n` as open ended to illustrate that the last massif is always in the process of being *appended* to.

[Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) gives you a shortcut for picking the right massif.
It can also be fairly easily computed from only the `merklelog_entry.commit.index` *mmrIndex* on your event using the example javascript on that page.

Here we deal with the format of a single massif.

## Every massif blob is a series of 32 byte aligned fields

Every massif in a log is structured as a series of `32` byte fields.
All individual entries in the log are either exactly 32 bytes or a small multiple of `32`.

```
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

Given a tenant identity of `72dc8b10-dde5-43fe-99bc-16a37fd98c6a` that tenants first massif blob can be found at:

**https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/72dc8b10-dde5-43fe-99bc-16a37fd98c6a/0/massifs/0000000000000000.log**

Each massif is stored in a numbered file. The filename is the 16-character, zero-padded, massif index.

The datatrails attestation for each massif can be found at a closely associated url. For the massif above it is

**https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/72dc8b10-dde5-43fe-99bc-16a37fd98c6a/0/massifseals/0000000000000000.sth**

These paths are served via a simple reverse proxy to the native azure commodity storage where your logs are stored. The full [Azure REST API](https://learn.microsoft.com/en-us/rest/api/azure/) for getting specific massif blobs can be utilised. For reasons of cost all operations are subject to rate limits, listing blobs is not possible, though filtering blobs by tags is permitted. Both the massif blobs and the log seal blobs are always tagged with the most recent idtimestamp for the log. In the case of the masssif blobs, it is the idtimestamp most recently added to the log. In the case of the seal blob it is the most recent log entry that has been attested by datatrails. The tag name is `lastid`


## When re-creating inclusion proofs, you are guaranteed to only need a single massif

The variable section of the massif blob is further split into *look back* nodes, and regular massif nodes:

```
+----------------+----------------+
| FIXED          | HEADER DATA    |
|                +----------------+  fixed size
|        SIZE    | TRIE-DATA      |  pre-filled with zeros, populated as leaves are added
+----------------+----------------+
| VARIABLE       | PEAK           | "look back nodes" write once
|                |         STACK  |   on massif create
|                +----------------+
|                | MMR            | grows until 2^(height-1) leaves are added
.                .   NODES        |
.   APPEND ONLY  .                |
+----------------+----------------+
```

{{< note >}}TODO: check that the formatting of this table is OK{{< /note >}}
We provide convenience look up tables for these [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables)

As mentioned above, we provide implementations of the algorithms needed to produce those tables in many languages under an MIT license.

## The first 32 byte field in every massif is the sequencing header

Using the following curl command, you can read the version and format information from the header field 0

```bash
curl -s \
  -H "Range: bytes=0-31" \
  -H "x-ms-blob-type: BlockBlob" \
  -H "x-ms-version: 2019-12-12" \
https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/7dfaa5ef-226f-4f40-90a5-c015e59998a8/0/massifs/0000000000000000.log | od -An -tx1 | tr -d ' \n'

00000000000000008f01a7bb5d0cbb0000000000000000000000010e00000000
```

Note that this request requires no authentication or authorization.

The structure of the header field is:

```output
| type| idtimestamp| reserved |  version | epoch  |massif height| massif i |
| 0   | 8        15|          |  21 - 22 | 23   26|27         27| 28 -  31 | start and end byte indices, closed range
| 1   |     8      |          |      2   |    4   |      1      |     4    | count of bytes
```

The idtimestamp of the last leaf entry added to the log is always set in the header field.

You can see from the hex data above, that the idtimestamp of the last entry in the log is `8e84dbbb6513a600`[^2], the version is 0, the timestamp epoch is 1, the massif height is 14, and the massif index is 0.

[^2]: The idtimetamp value is 64 bits, of which the first 40 bits are a millisecond precision time value and the remainder is data used to guarantee uniqueness of the timestamp. We use a variant of the [Snowflake ID](https://en.wikipedia.org/wiki/Snowflake_ID) scheme. Our implementation can be found at [nextid.go](https://github.com/datatrails/go-datatrails-merklelog/blob/main/massifs/snowflakeid/nextid.go#L118)

### Decoding an idtimestamp

The idtimestamp is 40 bits of time at millisecond precision.
The idtimestamp in the header field is always set to the idtimestamp of the most recently added leaf.

{{< tabs name="convert idtimestamp" >}}
   {{< tab name="Python" >}}

   ```python
   import datetime

   epoch=1
   unixms=int((
      bytes.fromhex("8e84dbbb6513a600")[:-3]).hex(), base=16
      ) + epoch*((2**40)-1)
   datetime.datetime.fromtimestamp(unixms/1000)

   datetime.datetime(2024, 3, 28, 11, 39, 36, 676000)
   ```

  {{< /tab >}}
{{< /tabs >}}

In this example, the last entry in the log (at that time) was 2024/03/28, a little after 11.30 am.

## The trieData entries are 512 bits each and are formed from two fields

With the trie keys, full data recovery can be verified without needing to remember the order that events were added to the log.

Massifs can be recovered independently even if the data for other massifs is incomplete.

The index also provides for proof of exclusion. Proof that a specific event is not in the index. As the event identities contribute to both the index keys and the leaf entries, and as the keys are time ordered on addition, it is possible to audit the specific range.
This will confirm the log is consistent with the index for the time range in which the disputed item is claimed to exist.


The trieData section is 2 * 32 * 2<sup>height</sup> bytes long. (Which is exactly double what we need).  For the standard massif height of 14, it has 8192 entries in the first 524288 bytes. The subsequent 524288 will always be zero.

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

```
0                                                        31
SHA256(BYTE(0x00) || tenant-identity || event.identity)
0                                       BYTES(IDTIMESTAMP)
32                                      56               63
```

Described in further detail in the [term-cheatsheet](https://github.com/datatrails/go-datatrails-merklelog/blob/main/term-cheatsheet.md#trie-entry)

Note that the inclusion of your tenant identity in the hash makes the entry unique to your tenant. So even when sharing events with other tenants, this will not correlate directly with activity in their logs.

When a massif is initialized the trieData is pre-populated for all leaves and set to all zero bytes. As events are recorded in the log, the zero-padded index is filled in.

A sub-range of field 0 will change when saving the last idtimestamp in it. The mmr node values are strictly only ever appended to the blob. Once appended they will never change and they will never move.


Returning to the trieData section, If your event identity was

  `assets/87dd2e5a-42b4-49a5-8693-97f40a5af7f8/events/a022f458-8e55-4d63-a200-4172a42fc2a`

Then its trieKey would be

`eda55087407b2e6f52c668f039c624d2382422ea8c765d618a0bbbef2936223d`

The following python snippet would generate it from your event data should you wish to confirm what should be in the index at a specific position.

{{< tabs name="triekey" >}}
   {{< tab name="Python" >}}

   ```python
  def triekey(tenant, event):
      h = hashlib.sha256()
      h.update(bytes([0]))
      h.update(tenant.encode())
      h.update(event.encode())
      return h.hexdigest()
   ```
  {{< /tab >}}
{{< /tabs >}}

Then,

```python
print(triekey(
   "tenant/7dfaa5ef-226f-4f40-90a5-c015e59998a8",
   "assets/87dd2e5a-42b4-49a5-8693-97f40a5af7f8/events/a022f458-8e55-4d63-a200-4172a42fc2aa"))

```

Will output

'eda55087407b2e6f52c668f039c624d2382422ea8c765d618a0bbbef2936223d'

This example is an event on a public asset, so it can also be found in the
public tenant's merkle log

Again we use curl, this time to fetch the public tenants log,

```bash
curl -s \
  -H "x-ms-blob-type: BlockBlob" \
  -H "x-ms-version: 2019-12-12" \
  https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifs/0000000000000000.log -o mmr.log
```

And we can obtain the trie key for the same event shared into the public
tenant:

```python
print(triekey(
   "tenant/6ea5cd00-c711-3649-6914-7b125928bbb4",
   "assets/87dd2e5a-42b4-49a5-8693-97f40a5af7f8/events/a022f458-8e55-4d63-a200-4172a42fc2aa"))
```
Which is: `6372ef3f14a643fb00d24f5fef11c0bf796fb0dde48bbfa8cc4d08b400be2385`


Noting that we do not include the 'public' routing prefix on the event identity.

This works the same for regular OBAC shares.

It is not possible to directly correlate activity between different tenants logs unless you know both the tenant identity and the event identity. For permissioned events, this will only be available to you if you are included in the sharing policy. The idtimestamp is different for each log, guaranteed unique within the context of a single log, and, assuming only good operation of our cloud providers clocks, guaranteed unique system wide.

It is important to remember that timing analysis is possible regardless of whether we have trie keys or not.

## The peak stack and mmr data sizes are computable.

See [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) to avoid needing to calculate these.
Implementations of the O(log base 2 n) algorithms are provided in various languages.
They all have very hardware-sympathetic implementations.

## The massif height is constant for all blobs in a log *configuration*

For massif height 14, the fixed size portion is `1048864` bytes.

A typical url for a massif storage blob looks like:

https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/7dfaa5ef-226f-4f40-90a5-c015e59998a8/0/massifs/0000000000000000.log

In the above, the *log configuration* identifier is the `/0/` between the tenant uuid and the `massifs/0000000000000000.log`

We record the massif height in the start record of every massif. And we guarantee that all massifs in a single configuration path have the same **massif height**.

Currently all tenants use the same configuration.

In the future, DataTrails may re-size your massifs. In a log reconfiguration activity, we would first publish the tail of the log to the new path, eg `/1/massifs/0000000000000123.log`. The log is instantly available for continued growth. The historic configuration continues to be available under the `/0/` path. And, depending on data retention and migration policies for your tenant, the historic configuration can verifiably be migrated to the new path without interrupting service or availability.

We can do this without impacting the verifiability of the contained data and without invalidating your previously cached copies taken from the earlier massif size configuration. In the event that we do re-configure in this way, a log configuration description will also be published along side the massifs and seals.

Simple binary file compare operations can show that the verifiable data for the new configuration is the same as in the original should you wish to assure yourself of this fact.

The previous configuration path will no longer receive any additions.

{{< note >}}
For the foreseeable future (at least months) we don't anticipate needing to do this.
{{< /note >}}

## How to read a specific mmr node by its *mmrIndex*

The variable portion *for the first massif* contains exactly *16383* MMR *nodes*.
Of those nodes, *8192* are the leaf entries in the Merkle tree corresponding to your events.

If you know the byte offset in the blob for the start of the mmr data then you can check the number of mmr nodes currently in it by doing `(blobSize - mmrDataStart)/32`.

Find the smallest "Last Node" in [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) that is greater than your *mmrIndex* and use that row as your massif index

Then taking massif index 0 (row 0) for example, and using the first mmrIndex for ease of example, and working with the public tenant so we can all see the original event data.


**https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifs/0000000000000000.log**

```python
LOGSTART=1048864
MMRINDEX=0
curl -s \
-H "Range: bytes=$(($LOGSTART+$MMRINDEX*32))-$(($LOGSTART+$MMRINDEX*32+31))" \
-H "x-ms-blob-type: BlockBlob" \
-H "x-ms-version: 2019-12-12" \
https://app.datatrails.ai/verifiabledata/\
merklelogs/v1/mmrs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifs/\
0000000000000000.log  | od -An -tx1 | tr -d ' \n'

c771c6d578944e907d476d43766fb45ae9b63bbd7730f21c71a2fc8ab313547b
```

The [veracity](https://github.com/datatrails/veracity/blob/main/README.md#installation) tool can be used to confirm that

```bash
veracity \
  --url https://app.datatrails.ai/verifiabledata \
  --tenant tenant/6ea5cd00-c711-3649-6914-7b125928bbb4 \
  node -i 0

c771c6d578944e907d476d43766fb45ae9b63bbd7730f21c71a2fc8ab313547b
```

The example javascript routines below the [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) can be used to accomplish this computationally.

## The leaf nodes are created by hashing your event data

```
0                                                        31
SHA256(BYTE(0x00) || BYTES(IDTIMESTAMP) || V3-SCHEMA(event))
```

The V3 Schema defines how the content on your event is consistently converted to bytes prior to hashing.
This works by passing the fields specified in the schema through the [bencode](https://en.wikipedia.org/wiki/Bencode) encoding system.

See our knowledge base [article](https://support.datatrails.ai/hc/en-gb/articles/18120936244370-How-to-independently-verify-Merkle-Log-Events-recorded-on-the-DataTrails-transparency-ledger#h_01HTYDD6ZH0FV2K95D61RQ61ZJ) for an example in javascript and the definition of the V3 fields.

Note that this includes the event_identity and tenant_identity which are also included in the trieKey hash.

The remaining item is conditioning the `IDTIMESTAMP` for hashing.

If you have the event record from the Events API, the idtimestamp is found at `merklelog_entry.commit.idtimestamp`.
It is a hex string and prefixed with `01` which is the epoch from the header.

To condition the string value, strip the leading `01` and convert the remaining hex to binary.
Then substitute those bytes, in presentation order, for idTimestamp above.

The bytes for the hash are just `bytes.fromhex("018e84dbbb6513a6"[2:])`


If you want the actual unix millisecond timestamp you can do this:
```python
epoch = 1
unixms=int((
  bytes.fromhex("018e84dbbb6513a6"[2:])[:-2]).hex(), base=16
  ) + epoch*((2**40)-1)
```

## But which nodes would I want ?

Typically, you would be verifying the inclusion of an event in the log.
This inclusion is verified by selecting the sibling path needed to recreate the root hash starting from your leaf hash.
You create your leaf hash using the original pre-image data of your event and the *commit* values assigned to it when it was included in the log.

You would have:

* The V3 canonical set of fields from your event (as described in our knowledge base [article](https://support.datatrails.ai/hc/en-gb/articles/18120936244370-How-to-independently-verify-Merkle-Log-Events-recorded-on-the-DataTrails-transparency-ledger#h_01HTYDD6ZH0FV2K95D61RQ61ZJ))
* The `merklelog_entry.commit.index` (the mmrIndex of the event in the log)
* The `merklelog_entry.commit.idtimestamp` uniquely placing the record of the log in time (according to our cloud service provider)

We are going to give the subject of determining the sibling path its own article. Here we are going to set the scene by covering how our logical tree nodes map to storage.

So what is a sibling path?
To understand this we need to dig into how we organize the nodes in your Merkle log in storage and memory.

## The tree maps to storage like this

Merkle trees, at their heart, *prove* things by providing paths of hashes that lead to a single *common root* for all nodes in the tree. For an MMR, a single root can be produced by "bagging the peaks". But the list of peaks, from which that single root is produced, is itself precisely determined by the size of the mmr. Having the peak list is equivalent to having a single root. And having a path that leads to a peak is equivalent to having a path to a single root. The peak list is an accumulator state and a path to an accumulator is actually more useful.

The formal details, and a very nice visualization of how the peaks combine, is available in this paper on
[cryptographic, asynchronous, accumulators](https://eprint.iacr.org/2015/718.pdf) (see Fig 4, page 12)

The peaks are exactly the accumulator described there.

All entries in a Merkle log each have a unique and *short* path of hashes[^3]: , which when hashed together according to the data structures rules, will re-create the same root (or lead to the same accumulator entry).
If such a path does not exist, then by definition the leaf is not included - it is not in the log.

[^3]: Such a path of hashes is commonly referred to as a "proof", a "witness", and an "authentication path". A Merkle Tree is sometimes referred to as authenticated data structures or a verifiable data structure. For the purposes of this article, there is no meaningful difference. They are all the same thing. We stick to "verification" and "verifiable data structure" in this article.

Where do those paths come from?
They come from adjacent and ancestor nodes in the hierarchical tree. And this means that when producing the path we need to access nodes throughout the tree to produce the proof.

Using our "canonical" mmr log for illustration, we get this diagram, the vertical axis is labeled by height index, which is just height - 1. The connecting diagonal dashes above the "tree line" indicate nodes that belong to one massif but depend on nodes in earlier massifs.

```output
                       14 we call these the 'spur' nodes, as they each depend on ancestor nodes
                          \
                6           13             22        (affectionately called the alpine zone)
                  \            \             \
        1 |  2  |  5  |   9  |  12  |  17  | 21  | -- massif 'tree line'
          |     |     |      |      |      |     |
        0 |0   1| 3  4| 7   8|10  11|15  16|18 19|
          |-----|-----|------|------|------|-----|
          |  0  |  1  |  2   |   3  |   4  |  5  | MASSIF's
```

The sibling *proof* path for the leaf with `mmrIndex` 7 would be [8, 12, 6], and the "peak bagging" algorithm would then be applied to get the root if that was desired.

```output
H(7 || 8) = 9
H(9 || 12) = 13
H(6 || 13) = 14
```

14 is a peak in the MMR. The precise set of peaks are determined exclusively from the current mmr size which is 23 in this case. Showing a leaf has a path to a peak for the MMR is sufficient to prove its inclusion in the MMR.

## The "look back" peak stack can be visualized like this

A specific challenge for log implementations with very large data sets is  answering "how far back" or "how far forward" may I need to look?

MMRs differ from classic binary Merkle trees in how the incomplete sub-trees are combined into a common root.
For an MMR, the common root is defined by an algorithm for combining the adjacent, incomplete sub-trees.
Rather than by the more traditional, temporary, assignment of un-balanced siblings.
Such un-balanced siblings would later have to be re-assigned (balanced) when there were sufficient leaves to merge the sub-trees.

While a single root can be produced for an MMR, due to the properties of the accumulator construction, there is much less value in doing so. Typically, verification use cases are better served by paths to an accumulator.

This detail is what permits us to publish the log data immediately that your events are added to the log.

So the specific properties of Merkle Mountain Ranges lead to an efficiently computable and stable answer to the question of "which other nodes do I need".  Such that we *know* categorically that we do not need to look *forward* of the current massif and further we know precisely which nodes we need from the previous massifs.

The "free nodes" in the alpine zone always require "ancestors" from previous nodes when producing inclusion proofs that pass through them and when adding new nodes to the end of the log. But those ancestors are precisely the peaks forming the accumulator that we want anyway so we can attest to the log state and provide efficient, permanently useful, proofs of inclusion and consistency.

The progression of the peak stack (accumulator) can be visualized like this. In this diagram we gather the dependent nodes into the massifs they belong too and carry forward the peak stack (accumulator) that fully authenticates the entire state of the MMR preceding the massif.

```output
      |[]   |[2]  |[6]   |[6,9]  |[14]   |[14,17]| peak stack
      |     |     |      |       |       |       |
      |     |6    |      |13, 14 |       |22     | spurs
      |     |     |      |       |       |       |
h=2 1 |  2  |  5  |   9  |  12   |  17   |  21   | <-- massif height 'tree line'
      |     |     |      |       |       |       |
    0 |0   1 3   4| 7   8|10   11|15   16|18   19|
```
_Note: height is 1 based, height indices are 0 based. So at h=2 we have height index 1._

The log configuration parameter massif height is the "tree line".
Essentially the first leaf addition that causes "break out" is the last leaf of that particular massif.  But those "break out nodes" for the last leaf are stored in the same massif as the leaf.  This means while the leaf count for each massif is fixed, the number of nodes is variable.  The variance is deterministic given only the MMR size.

We call the look-back nodes the *peak stack*, because the operations we use to maintain it are stack like.

We don't pop things off the peak stack once it is established at the creation of a new massif.
We just happen to reference it in reverse order of addition when adding new leaves.

The stability of the MMR data comes from the fact that the sub trees are not merged until a right sibling tree of equal height has been produced. This means when we merge, the sub trees do not change in content or organisation, nodes are simply appended to commit them to the log. This results in the "write-once" and "append only" properties discussed in the [crosby-wallach](https://static.usenix.org/event/sec09/tech/full_papers/crosby.pdf) 3.3 "Storing the log on secondary storage"

## How the tree spans the massifs

A worked example for a Merkle log whose height configuration parameter is set to 2.

## Massif 0

The peak stack size is established for a massif when it is created in its empty state. The size is efficiently calculable from the MMR Index at the start of the new massif. For the first massif the stack will be empty.

When viewed horizontally, we start by denoting the empty stack like this.

```
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

### massif 1

The global tree once massif 1 has been constructed is

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

We can see that for massif 1, the peak stack is [2].
We can also see that when we added node 4, the "back fill nodes" were added to "complete the tree" and that they were also stored in massif 1. The "break out" nodes visually overhang the previous massif, but are stored in massif 1.

This layout is also known as a "post order" traversal of a binary tree.

Note that the addition of node 6, while backfilling for 4, requires node 2 from the previous massif 0.  This is why it is carried forward in the peak stack.

We can also see that is the *only* node that is required from massif 0 for *any* verification path in massif 1.

As the log grows, the accumulator (peak stack) moves on.  However, historic verification paths can always be proven to exist in all future accumulators.  If you have a pair of signed accumulators that are not consistent with this, you have evidence the log is broken.

The key point here is that, in massif 1, when computing a verification path for nodes 3 or 4, the only node that is required from massif 0 is available locally in the peak stack (in massif 1).

This means that should you lose interest in the leaf entries from massif 0, the whole massif can be deleted without fear that it will impact the verifiability of subsequent items in the log.

If you retain the seal from massif 0, or if you can count on it being available from another trusted source, you only strictly need to retain leaves of interest and their verification paths.

### massif 2

The global tree at the end of massif 2

```output
2       6
          \
1    2  |  5  |  9  |
    / \ |/  \ | / \ |
   0   1|3   4|7   8|
   -----|-----|-----|
     0  |  1  |  2  | MASSIF
```
The layout for massif 2, showing the peak stack is [6]
```output
+---++---+---+---+
| 6 || 7 | 8 | 9 |
+---++---+-------+
```

Note that 6 has replaced 2. The 2 is not required for any verification path
for elements added in massif 2 or beyond.

### massif 3

The global tree at the end of massif 3

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

The peak stack is [6, 9]. Because both nodes 6 and 9 were needed to complete
the MMR that includes leaf node 11.

```output
+---+---++----+----+----+----+----+
| 6 | 9 || 10 | 11 | 12 | 13 | 14 |
+---+---++----+----+----+----+----+
```

### massif 4

The global tree at the end of massif 4

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

So the peak stack is [14], discarding 6 and 9, and the massif 4 layout is:

```output
+---++----+----+----+
| 14|| 15 | 16 | 17 |
+---++----+----+----+
```

## Takeaways

* Merkle logs are divided into massifs, each of which stores verification data for a fixed number of your events.
* Once verification data is written to the log, it never changes.
* The "look back" nodes needed to make each massif self contained are deterministic and are filled in when a new massif is started.
* The dynamically sized portions of the format are all computable, but we offer pre-calculated tables for convenience.
* Open-source tooling exists in multiple languages for navigating the format.
* Once you have a signed accumulator (or root), all entries in any copies of your log are irrefutably attested by DataTrails

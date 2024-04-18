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

DataTrails publishes the data necessary for verifying events immediately to publicly readable and highly available commodity cloud storage.
We call this verifiable data your *log* or *transparency log*.

Once verifiable data is written to this log we never change it.
The log only grows, it never shrinks and data in it never moves.

[DataTrails provides extensive open-source tooling](<url>) to work with this format in an offline setting.

To take advantage of this you will need:

1. A copy of the section of the log containing your event.
1. A copy of any log *seal* from *any* time after your event was included.
1. A copy of any events you wish to verify (that you retained or that you later retrieved).

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
Merkle Mountain Ranges are attributed to [Peter Todd](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-May/012715.html), though much parallel invention has occurred.
They have been independently analyzed in the context of [cryptographic asynchronous accumulators](https://eprint.iacr.org/2015/718.pdf), Generalized multi-proofs for [Binary Numeral Trees](https://eprint.iacr.org/2021/038.pdf).
And also by the [ethereum research community](https://ethresear.ch/t/batching-and-cyclic-partitioning-of-logs/536).

Each massif contains the verifiable data for a fixed number, and sequential range, of your events.
The number of events is determined by your log configuration parameter `massif height`.
Currently, all logs have a massif height of `14` And the number of event *leaf* log entries in each massif is 2<sup>height-1</sup>, which is 2<sup>14-1</sup> leaves, which is `8192` leaves [^2].

[^2]: Sometimes, DataTrails may re-size your massifs.
We can do this without impacting the verifiability of the contained data and without invalidating your previously cached copies taken from the earlier massif size configuration.
Simple binary file compare operations can show that the verifiable data for the new configuration is the same as in the original should you wish to assure yourself of this fact.

Here, we have drawn `massif n` as open ended to illustrate that the last massif is always in the process of being *appended* to.

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

{{< note >}}TODO: change this tenant identity for a production tenant. This one is from a testing environment{{< /note >}}
Given a tenant identity of `72dc8b10-dde5-43fe-99bc-16a37fd98c6a` that tenants first massif blob can be found at:

**https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/72dc8b10-dde5-43fe-99bc-16a37fd98c6a/0/massifs/0000000000000000.log**

This is a simple reverse proxy to the native azure blob store where your logs are stored:

**https://jitavidfd1103b1099ab3aa.blob.core.windows.net/merklelogs/v1/mmrs/tenant/**

Each massif is stored in a numbered file.
The filename is the 16-character, zero-padded, massif index.

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
https://jitavidfd1103b1099ab3aa.blob.core.windows.net/merklelogs/\
v1/mmrs/tenant/73b06b4e-504e-4d31-9fd9-5e606f329b51/0/massifs/\
0000000000000000.log | od -An -tx1 | tr -d ' \n'

00000000000000008e84dbbb6513a60000000000000000000000010e00000000
```

Note that this request requires no authentication or authorization.

The structure of the header field is:

```output
| type| idtimestamp| reserved |  version | epoch  |massif height| massif i |
| 0   | 8        15|          |  21 - 22 | 23   26|27         27| 28 -  31 |
| 1   |     8      |          |      2   |    4   |      1      |     4    |
```

The idtimestamp of the last leaf entry added to the log is always set in the header field.

You can see from the hex data above, that the idtimestamp of the last entry in the log is `8e84dbbb6513a6`, the version is 0, the timestamp epoch is 1, the massif height is 14, and the massif index is 0.

### Decoding an idtimestamp

The idtimestamp is 40 bits of time at millisecond precision.
The idtimestamp in the header field is always set to the idtimestamp of the most recently added leaf.

{{< tabs name="convert idtimestamp" >}}
   {{< tab name="Python" >}}

   ```python
   import datetime

   epoch=1
   unixms=int((
      bytes.fromhex("8e84dbbb6513a6")[:-2]).hex(), base=16
      ) + epoch*((2**40)-1)
   datetime.datetime.fromtimestamp(unixms/1000)
   
   datetime.datetime(2024, 3, 28, 11, 39, 36, 676000)
   ```

  {{< /tab >}}
{{< /tabs >}}

In this example, the last entry in the log (at that time) was 2024/03/28, a little after 11.30 am.

## The trieData entries are 512 bytes each and are formed from two fields

The trieData section is 2 * 32 * 2<sup>height</sup> bytes long. (Which is exactly double what we need).
For the standard massif height of 14, it has 8192 entries in the first 524288 bytes.
The subsequent 524288 will always be zero.
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
SHA256(BYTE(0x00) || BYTES(idTimestamp) || event.identity)
0                                       BYTES(IDTIMESTAMP)
32                                      56               63
```

Note that the idtimestamp is unique to your tenant and the wider system, so even when sharing events with other tenants, this will not correlate directly with activity in their logs.

If you have the event record from the Events API, the idtimestamp is found at `merklelog_entry.commit.idtimestamp`.
It is a hex string and prefixed with `01` which is the epoch from the header.

To condition the string value, strip the leading `01` and convert the remaining hex to binary.
Then substitute those bytes, in presentation order, for idTimestamp above.

Reworking our python example above to deal with the epoch prefix would look like this:

```python
epoch = 1
unixms=int((
  bytes.fromhex("018e84dbbb6513a6"[2:])[:-2]).hex(), base=16
  ) + epoch*((2**40)-1)
```

And the bytes for the hash are just `bytes.fromhex("018e84dbbb6513a6"[2:])`

If your event identity was

  `assets/31de2eb6-de4f-4e5a-9635-38f7cd5a0fc8/events/21d55b73-b4bc-4098-baf7-336ddee4f2f2`

Then its trieKey would be

`b8e04443d64b8f1603fff250952b29e71d6c2d221afd8d60dec133c63e7325d9`

The following python snippet would generate it from your event data should you wish to confirm what should be in the index at a specific position.

```python
h = hashlib.sha256()
h.update(bytes([0]))
h.update(bytes.fromhex("018e84dbbb6513a6"[2:]))
h.update("assets/31de2eb6-de4f-4e5a-9635-38f7cd5a0fc8/events/21d55b73-b4bc-4098-baf7-336ddee4f2f2".encode())
h.hexdigest()
```

The variable portion *for the first massif* contains exactly *16383* MMR *nodes*.
Of those nodes, *8192* are the leaf entries in the Merkle tree corresponding to your events.

When a massif is initialized the trieData is pre-populated for all leaves and set to all zero bytes.
As events are recorded in the log, the zero-padded index is filled in.
A sub-range of field 0 will change when saving the last idtimestamp in it.
The mmr node values are strictly only ever appended to the blob.
Once appended they will never change and they will never move.

If you know the byte offset in the blob for the start of the mmr data then you can check the number of mmr nodes currently in it by doing `(blobSize - mmrDataStart)/32`.

## The peak stack and mmr data sizes are computable.

See [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) to avoid needing to calculate these.
Implementations of the O(log base 2 n) algorithms are provided in various languages.
They all have very hardware-sympathetic implementations.

## The massif height is constant for all blobs in a log *configuration*

For massif height 14, the fixed size portion is `1048864` bytes.

All massifs in a log are guaranteed to be the same *height*.
If your log is re-configured having first been available at

`https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/72dc8b10-dde5-43fe-99bc-16a37fd98c6a/0/`

Then on re-configuration it will become available (without downtime) at:

`https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/72dc8b10-dde5-43fe-99bc-16a37fd98c6a/1/`

And the previous path will no longer receive any additions.

{{< note >}}
For the forseeable future (at least months) we don't anticipate needing to do this.
{{< /note >}}

## How to read a specific mmr node by its *mmrIndex*

Find the smallest "Last Node" in [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) that is greater than your *mmrIndex* and use that row as your massif index

Then taking massif index 0 (row 0) for example, and using the first mmrIndex for ease of example

```python
LOGSTART=1048864
MMRINDEX=0
curl -s \
-H "Range: bytes=$(($LOGSTART+$MMRINDEX*32))-$(($LOGSTART+$MMRINDEX*32+31))" \
-H "x-ms-blob-type: BlockBlob" \
-H "x-ms-version: 2019-12-12" \
https://jitavidfd1103b1099ab3aa.blob.core.windows.net/\
merklelogs/v1/mmrs/tenant/73b06b4e-504e-4d31-9fd9-5e606f329b51/0/massifs/\
0000000000000000.log  | od -An -tx1 | tr -d ' \n'

a45e21c14ee5a0d12d4544524582b5feb074650e6bb2b31ed9a3aeffe4883099
```

The veracity demo tool can be used to confirm that

```bash
go run veracity/cmd/veracity/main.go -s jitavidfd1103b1099ab3aa \
 -t tenant/73b06b4e-504e-4d31-9fd9-5e606f329b51 node -i 0

a45e21c14ee5a0d12d4544524582b5feb074650e6bb2b31ed9a3aeffe4883099
```

The example javascript routines below the [Massif Blob Pre-Calculated Offsets](/developers/developer-patterns/massif-blob-offset-tables) can be used to accomplish this computationally.

## But which nodes would I want ?

Typically, you would be verifying the inclusion of an event in the log.
This inclusion is verified by selecting the sibling path needed to recreate the root hash starting from your leaf hash.
You create your leaf hash using the original pre-image data of your event and the *commit* values assigned to it when it was included in the log.

You would have:

* The V3 canonical set of fields from your event
* The `merklelog_entry.commit.index` (the mmrIndex of the event in the log)
* The `merklelog_entry.commit.idtimestamp` uniquely placing the record of the log in time (according to our cloud service provider)

We are going to give the subject of determining the sibling path its own article. Here we are going to set the scene by covering how our logical tree nodes map to storage.

So what is a sibling path?
To understand this we need to dig into how we organize the nodes in your Merkle log in storage and memory.

## The tree maps to storage like this

Merkle trees, at there heart, *prove* things by providing paths of hashes that lead to a single *common root* for all nodes in the tree.

All entries in a Merkle log each have a unique and *short* path of hashes, which when hashed together according to the data structures rules, will re-create the same root.
If such a path does not exist, then by definition the leaf is not included - it is not in the log.

Where do those paths come from?
They come from adjacent and ancestor nodes in the hierarchical tree.
And this means that when producing the path we need to access nodes throughout the tree to produce the proof.

Using our "canonical" mmr log for illustration, we get this diagram

```output
                       14 we call these the 'spur' nodes, as they each depend on ancestor nodes
                          \
                6           13             22        (affectionately called the alpine zone)
                  \            \              \
    h=2 1 |  2  |  5  |   9  |  12   |  17   | 21  | -- massif 'tree line'
          |     |     |      |       |       |     |
        0 |0   1| 3  4| 7   8|10   11|15   16|18 19|
```

The sibling *proof* path for the leaf with `mmrIndex` 7 would be [8, 12, 6], and the "peak bagging" algorithm would then be applied to get the root.

A very nice visualization of how the peaks combine is available in this paper on
[cryptographic, asynchronous, accumulators](https://eprint.iacr.org/2015/718.pdf) (see Fig 4, page 12)

## The "look back" peak stack can be visualized like this

A specific challenge for log implementations with very large data sets is  answering "how far back" or "how far forward" may I need to look?

MMRs differ from classic binary Merkle trees in how the incomplete sub-trees are combined into a common root.
For an MMR, the common root is defined by an algorithm for combining the adjacent, incomplete sub-trees.
Rather than by the more traditional, temporary, assignment of un-balanced siblings.
Such un-balanced siblings would later have to be re-assigned (balanced) when there were sufficient leaves to merge the sub-trees.

This detail is what permits us to publish the log data immediately that your events are added.

So the specific properties of Merkle Mountain Ranges lead to an efficiently computable and stable answer to the question of "which other nodes do I need".
Such that we *know* categorically that we do not need to look *forward* of the current massif and further we know precisely which nodes we need from the previous massifs.

The "free nodes" in the alpine zone always require "ancestors" from previous nodes when producing inclusion proofs that pass through them, and when adding new nodes to the end of the log.
Here we can see they are very predictable (can be calculated without reference to the tree data).
We accumulate these peaks in a stack because the pop order is the order we need them when adding leaves at the end of the log.

The result can be visualized like this

```output
      |[]   |[2]  |[6]   |[6,9]  |[14]   |[14,17]| peak stack
      |     |     |      |       |       |       |
      |     |6    |      |13, 14 |       |22     | spurs
      |     |     |      |       |       |       |
h=2 1 |  2  |  5  |   9  |  12   |  17   |  21   | <-- massif 'tree line'
      |     |     |      |       |       |       |
    0 |0   1 3   4| 7   8|10   11|15   16|18   19|
```

We call the look-back nodes the *peak stack*, because it always corresponds to the peaks of the earlier sub-trees.
We don't pop things off it ever, we just happen to reference it in reverse order of addition when adding new leaves.

The stability of the MMR data comes from the fact that the sub trees are not merged until a right sibling tree of equal height has been produced.

## How the tree spans the massifs

A worked example for a Merkle log whose height configuration parameter is set to 2.

### Massif 0

Viewed horizontally, and only considering the peak stack and the mmr nodes, the first massif, in our canonical example, will look like this

```output
++---+---+---+
|| 0 | 1 | 2 |
++---+-------+
```

The massif has exactly 3 nodes

The peak stack is empty

```output
  1    2  | --- massif tree line massif height index = 2-1
      / \ |
     0   1| MMR INDICES
     -----|

++---+---+---+
|| 0 | 1 | 2 |
++---+-------+
```

### massif 1

The peak stack is [2]

```output
2       6
         \
1    2  | 5   | --- massif tree line massif height index = 2-1
    / \ |/  \ |
   0   1|3   4| MMR INDICES
   -----|-----|

+---++---+---+---+---+
| 2 || 3 | 4 | 5 | 6 |
+---++---+-------+---+
```

### massif 2

The peak stack is [6]

```output
2       6
          \
1    2  |  5  |  9  |
    / \ |/  \ | / \ |
   0   1|3   4|7   8|

+---++---+---+---+
| 6 || 7 | 8 | 9 |
+---++---+-------+
```

### massif 3

The peak stack is [6, 9]

```
                 14
                   \
                    \
                     \
  2        6          13
            \           \
  1    2  |  5  |  9  |  \   |
      / \ |/  \ | / \ |  12  |
     0   1|3   4|7   8|  /  \|

+---+---++----+----+----+----+----+
| 6 | 9 || 10 | 11 | 12 | 13 | 14 |
+---+---++----+----+----+----+----+
```

### massif 4

Note that this case is particularly interesting because it completes a full cycle from one perfect power-sized tree to the next.
A fact of the MMR construction is the look back is never further than the most recent 'perfect' tree completing massif.

The peak stack is [14]

```output
3              14
                 \
                  \
                   \
2        6          13
          \           \
1    2  |  5  |  9  |  \    |  17  |
    / \ |/  \ | / \ |  12   | /  \ |
   0   1|3   4|7   8|  /  \ |15  16|

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
* Once you have a signed "root", all entries in any copies of your log are irrefutably attested by DataTrails

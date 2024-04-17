---
 title: "Massif blob pre-calculated offsets"
 description: "Provides pre calculated tables for navigating raw Merkle logs"
 lead: "Lookup tables for navigating the dynamic, but computable, offsets into the Merkle log binary format"
 draft: false
 images: []
 menu:
   developers:
     parent: "developer-patterns"
 weight: 34
 toc: true
---

This page provides lookup tables for navigating the dynamic, but computable, offsets into the Merkle log binary format.
The algorithms to reproduce this are relatively simple.
We provide open-source implementations, but in many contexts, it is simpler to use these pre-calculations.
These tables can be made for any log configuration at any time, in part or in whole, without access to any specific log.

This is a fast review of the log format. We explain this in more detail at [Navigating the Merkle Log](/developers/developer-patterns/navigating-merklelogs)

## Each log is comprised of many blobs, each containing a fixed number of leaves

    +----------------+ +----------------+ .. +-----------+
    |     massif 0   | |     massif 1   |    |  massif n
    +----------------+ +----------------+ .. +-----------+

New leaves are added to the last blob in the log.

## Each individual blob has a fixed size portion and two variably sized sections

    |--------.----------.----------.---------|
    |  fixed  size      | computable size    |
    |--------.----------.----------.---------|
    | header | trieData |peak stack| mmrData |
    |--------.----------.----------.---------|


## The peak stack and mmr data sizes are computable

...but it is not always convenient to do so.


Using the `veracity` tool with the following command line we can reproduce our canonical "illustrative" log from [Navigating the Merkle Log](/developers/developer-patterns/navigating-merklelogs)


                       14
                          \
                6           13             21
                  \            \              \
    h=2 1 |  2  |  5  |   9  |  12   |  17   | 20  |
          |     |     |      |       |       |     |
        0 |0   1| 3  4| 7   8|10   11|15   16|18 19| MMR INDICES
        0 |0   1| 2  3| 4   5|6     7|8     9|10 11| LEAF INDICES


    go run veracity/cmd/veracity/main.go --height 2 massifs --count 6



In the following table *Stack Start* and *mmr Start* are byte offsets from the start of the file.
The leaf values are indices into the trie fields (not considered further in this page) and the node values are indices into the array of 32-byte nodes starting at *mmr Start*

| Massif | Stack Start| mmr Start |  First leaf | Last Leaf | First Node  | Last Node | Peak Stack |
| -------| ---------- | --------- | ---------- | ---------- | ----------- | --------- | ---------  |
|       0|     544    |     544   |       0    |       1    |       0     |       2   | []
|       1|     544    |     576   |       2    |       3    |       3     |       6   | [2]
|       2|     544    |     576   |       4    |       5    |       7     |       9   | [6]
|       3|     544    |     608   |       6    |       7    |      10     |      14   | [6,9]
|       4|     544    |     576   |       8    |       9    |      15     |      17   | [14]
|       5|     544    |     608   |      10    |      11    |      18     |      21   | [14,17]

It is fairly easy to validate the leaves and nodes by hand. The reproducing the
Stack Start needs details from [Navigating the Merkle Log](/developers/developer-patterns/navigating-merklelogs)


## Pre-computes for your first million events

| Massif | Stack Start| mmr Start |  First leaf | Last Leaf | First Node  | Last Node | Peak Stack |
| -------| ---------- | --------- | ---------- | ---------- | ----------- | --------- | ---------  |
|       0| 1048864| 1048864|       0|    8191|       0|   16382| []
|       1| 1048864| 1048896|    8192|   16383|   16383|   32766| [16382]
|       2| 1048864| 1048896|   16384|   24575|   32767|   49149| [32766]
|       3| 1048864| 1048928|   24576|   32767|   49150|   65534| [32766,49149]
|       4| 1048864| 1048896|   32768|   40959|   65535|   81917| [65534]
|       5| 1048864| 1048928|   40960|   49151|   81918|   98301| [65534,81917]
|       6| 1048864| 1048928|   49152|   57343|   98302|  114684| [65534,98301]
|       7| 1048864| 1048960|   57344|   65535|  114685|  131070| [65534,98301,114684]
|       8| 1048864| 1048896|   65536|   73727|  131071|  147453| [131070]
|       9| 1048864| 1048928|   73728|   81919|  147454|  163837| [131070,147453]
|      10| 1048864| 1048928|   81920|   90111|  163838|  180220| [131070,163837]
|      11| 1048864| 1048960|   90112|   98303|  180221|  196605| [131070,163837,180220]
|      12| 1048864| 1048928|   98304|  106495|  196606|  212988| [131070,196605]
|      13| 1048864| 1048960|  106496|  114687|  212989|  229372| [131070,196605,212988]
|      14| 1048864| 1048960|  114688|  122879|  229373|  245755| [131070,196605,229372]
|      15| 1048864| 1048992|  122880|  131071|  245756|  262142| [131070,196605,229372,245755]
|      16| 1048864| 1048896|  131072|  139263|  262143|  278525| [262142]
|      17| 1048864| 1048928|  139264|  147455|  278526|  294909| [262142,278525]
|      18| 1048864| 1048928|  147456|  155647|  294910|  311292| [262142,294909]
|      19| 1048864| 1048960|  155648|  163839|  311293|  327677| [262142,294909,311292]
|      20| 1048864| 1048928|  163840|  172031|  327678|  344060| [262142,327677]
|      21| 1048864| 1048960|  172032|  180223|  344061|  360444| [262142,327677,344060]
|      22| 1048864| 1048960|  180224|  188415|  360445|  376827| [262142,327677,360444]
|      23| 1048864| 1048992|  188416|  196607|  376828|  393213| [262142,327677,360444,376827]
|      24| 1048864| 1048928|  196608|  204799|  393214|  409596| [262142,393213]
|      25| 1048864| 1048960|  204800|  212991|  409597|  425980| [262142,393213,409596]
|      26| 1048864| 1048960|  212992|  221183|  425981|  442363| [262142,393213,425980]
|      27| 1048864| 1048992|  221184|  229375|  442364|  458748| [262142,393213,425980,442363]
|      28| 1048864| 1048960|  229376|  237567|  458749|  475131| [262142,393213,458748]
|      29| 1048864| 1048992|  237568|  245759|  475132|  491515| [262142,393213,458748,475131]
|      30| 1048864| 1048992|  245760|  253951|  491516|  507898| [262142,393213,458748,491515]
|      31| 1048864| 1049024|  253952|  262143|  507899|  524286| [262142,393213,458748,491515,507898]
|      32| 1048864| 1048896|  262144|  270335|  524287|  540669| [524286]
|      33| 1048864| 1048928|  270336|  278527|  540670|  557053| [524286,540669]
|      34| 1048864| 1048928|  278528|  286719|  557054|  573436| [524286,557053]
|      35| 1048864| 1048960|  286720|  294911|  573437|  589821| [524286,557053,573436]
|      36| 1048864| 1048928|  294912|  303103|  589822|  606204| [524286,589821]
|      37| 1048864| 1048960|  303104|  311295|  606205|  622588| [524286,589821,606204]
|      38| 1048864| 1048960|  311296|  319487|  622589|  638971| [524286,589821,622588]
|      39| 1048864| 1048992|  319488|  327679|  638972|  655357| [524286,589821,622588,638971]
|      40| 1048864| 1048928|  327680|  335871|  655358|  671740| [524286,655357]
|      41| 1048864| 1048960|  335872|  344063|  671741|  688124| [524286,655357,671740]
|      42| 1048864| 1048960|  344064|  352255|  688125|  704507| [524286,655357,688124]
|      43| 1048864| 1048992|  352256|  360447|  704508|  720892| [524286,655357,688124,704507]
|      44| 1048864| 1048960|  360448|  368639|  720893|  737275| [524286,655357,720892]
|      45| 1048864| 1048992|  368640|  376831|  737276|  753659| [524286,655357,720892,737275]
|      46| 1048864| 1048992|  376832|  385023|  753660|  770042| [524286,655357,720892,753659]
|      47| 1048864| 1049024|  385024|  393215|  770043|  786429| [524286,655357,720892,753659,770042]
|      48| 1048864| 1048928|  393216|  401407|  786430|  802812| [524286,786429]
|      49| 1048864| 1048960|  401408|  409599|  802813|  819196| [524286,786429,802812]
|      50| 1048864| 1048960|  409600|  417791|  819197|  835579| [524286,786429,819196]
|      51| 1048864| 1048992|  417792|  425983|  835580|  851964| [524286,786429,819196,835579]
|      52| 1048864| 1048960|  425984|  434175|  851965|  868347| [524286,786429,851964]
|      53| 1048864| 1048992|  434176|  442367|  868348|  884731| [524286,786429,851964,868347]
|      54| 1048864| 1048992|  442368|  450559|  884732|  901114| [524286,786429,851964,884731]
|      55| 1048864| 1049024|  450560|  458751|  901115|  917500| [524286,786429,851964,884731,901114]
|      56| 1048864| 1048960|  458752|  466943|  917501|  933883| [524286,786429,917500]
|      57| 1048864| 1048992|  466944|  475135|  933884|  950267| [524286,786429,917500,933883]
|      58| 1048864| 1048992|  475136|  483327|  950268|  966650| [524286,786429,917500,950267]
|      59| 1048864| 1049024|  483328|  491519|  966651|  983035| [524286,786429,917500,950267,966650]
|      60| 1048864| 1048992|  491520|  499711|  983036|  999418| [524286,786429,917500,983035]
|      61| 1048864| 1049024|  499712|  507903|  999419| 1015802| [524286,786429,917500,983035,999418]

## The algorithms backing the table generation

In combination with the format information at [Navigating the Merkle Log](/developers/developer-patterns/navigating-merklelogs) the pre-computed tables above can be generated using these examples.
DataTrails provides open source, go-lang based, tooling at [URL] (_[__]__ )

{{< tabs name="convert idtimestamp" >}}
  {{< tab name="Leaf Count and Massif Index" >}}

```javascript
function massifIndex(mmrIndex, massifHeight) {
  const nl =  Number(leafCount(mmrIndex + 1n));
  const f = Number(1n << massifHeight);
  const massifIndex = Math.floor(nl / f);
  return massifIndex;
}

// returns the number of leaves in the largest mmr whose size is <= the supplied size
function leafCount(mmrSize) {
  let pos = BigInt(mmrSize);
  if (pos == BigInt(0)) return 0n;
  let peakSize = ((1n << 64n) - 1n) >> BigInt(clz64(mmrSize));
  let peakMap = 0n;
  for (; peakSize > 0n;) {
    peakMap <<= 1n
    if (pos >= peakSize) {
      pos -= peakSize;
      peakMap |= 1n;
    }
    peakSize >>= 1n;
  }
  return peakMap;
}

function clz64(num) {
  if (!typeof num === 'bigint') throw new Error(`num must be bigint not ${typeof num}`);
  num = BigInt.asUintN(64, num);

  const hi = num >> 32n;
  let lz = Math.clz32(Number(hi));
  if (lz !== 0) return lz;
  const lo = Number((num & ((1n << 32n) - 1n)));
  return 32 + Math.clz32(lo);
}
```
  {{< /tab >}}
  {{< tab name="mmrIndex from leafIndex" >}}
```javascript
function treeIndex(iLeaf) {
  let sum = 0n; // Assuming iLeaf can be very large, use BigInt for accuracy.
  let i = BigInt(iLeaf); // Ensure iLeaf is treated as BigInt

  while (i > 0n) {
      const height = log2Uint64(i) + 1n;
      sum += spurSumHeight(height) + BigInt(height);
      const half = 1n << (height - 1n);
      i -= half;
  }

  return sum;
}

// spurSumHeight counts the interior 'spur' nodes required for the given height
function spurSumHeight(height) {
  height = BigInt(height); // Ensure height is treated as BigInt

  if (height === BigInt(0)) {
      return BigInt(0);
  }

  let sum = BigInt(0);
  for (let i = BigInt(1); i <= height - BigInt(1); i += BigInt(1)) {
      sum += (BigInt(1) << (height - BigInt(1) - i)) * i;
  }
  return sum;
}

function log2Uint64(num) {
  if (typeof num === 'bigint') {
      if (num <= 1n) return 0n; // log2(1) = 0 and log2(0) is undefined, handled as 0 for simplicity
      let log = 0n;
      while (num > 1n) {
          num >>= 1n;
          log += 1n;
      }
      return log;
  }

  if (num <= 1) return 0; // Similarly, handle log2(1) = 0 and log2(0) as 0
  return Math.floor(Math.log2(num));
}

```
  {{< /tab >}}
  {{< tab name="Peak Stack Length" >}}
```
/** Calculate the size of a massifs peak stack by passing the massifIndex in place of iLeaf */
function leafMinusSpurSum(iLeaf) {
  let sum = BigInt(iLeaf);
  iLeaf = sum >> BigInt(1);

  while (iLeaf > 0) {
      sum -= iLeaf;
      iLeaf >>= BigInt(1);
  }
  return sum;
}
```
  {{< /tab >}}
{{< /tabs >}}


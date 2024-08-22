---
title: "Veracity"
description: "Supporting independent verification of your events"
lead: "Exploring DataTrails' merkle log with Veracity"
date: 2024-08-22T19:35:35+01:00
lastmod: 2024-08-22T19:35:35+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 110
toc: true
aliases: 
  - /docs/developer-patterns/veracity/

---

## Overview
Veracity is an open-source command line tool developed by DataTrails. It lets you explore the merkle 
log and prove that your critical data is present and correct. By default it connects to the DataTrails 
service to obtain the relevant merkle log for verification. The offline mode verifies event data
against local copies of merkle logs demonstrating the decentralizability of the proof layer.

In this tutorial we'll explore how you can use Veracity to:
1. Prove the inclusion of events that matter in the DataTrails merkle log with `verify-inclusion`
2. Explore the DataTrails merkle log using the `node` command

{{< note >}}
**Note:** Veracity has a range of power-user commands that are beyond the scope of this tutorial. If
you'd like to know more, please see the [Veracity Repo](https://github.com/datatrails/veracity?tab=readme-ov-file)
{{< /note >}}

## Prerequisites
- [Downloaded and installed Veracity](https://github.com/datatrails/veracity/releases)

## Verifying Critical Event Data
DataTrails captures events that matter to your business and lets you prove what happened at a later 
date. Here are two walkthroughs showing how to perform the proof with Veracity for online and 
offline data scenarios. We're going to walk through an example of proving that a publicly attested event exists on the live DataTrails merkle log.

#### Setup
```sh
EVENT_ID=publicassets/046ad7b4-dc99-4f90-9511-d2fad2e72bed/events/fef3c753-52e5-406b-8e41-8a36a2cc4818
DATATRAILS_URL=https://app.datatrails.ai
TENANT_ID=tenant/6ea5cd00-c711-3649-6914-7b125928bbb4
```

We just set some variables that reference the public tenant in DataTrails and a public event that 
we'd like to verify the inclusion of. 

#### Loading the Event
```sh
curl -sL $DATATRAILS_URL/archivist/v2/$EVENT_ID > event.json
```

If you inspect the contents of `event.json` you will see something like this (some fields omitted
for salience.)
```json
{
  "identity": "publicassets/046ad7b4-dc99-4f90-9511-d2fad2e72bed/events/fef3c753-52e5-406b-8e41-8a36a2cc4818",
  "asset_identity": "publicassets/046ad7b4-dc99-4f90-9511-d2fad2e72bed",
  "tenant_identity": "tenant/ee52ae46-d4fb-4030-9888-4696ef4b27da",
  "event_attributes": {
    "arc_display_type": "Business Critical Action",
    "quality_system_ref": "1112345",
    "approval_status": "2",
    "arc_description": "An important event to your business"
  },
  "timestamp_declared": "2024-08-22T16:28:54Z",
  "timestamp_accepted": "2024-08-22T16:28:54Z",
  "timestamp_committed": "2024-08-22T16:29:04.130Z",
  "confirmation_status": "CONFIRMED",
  "merklelog_entry": {
    "commit": {
      "index": "5772",
      "idtimestamp": "01917aeb9103048500"
    },
    "confirm": {
      "mmr_size": "5774",
      "root": "Z5S0ewjARI26IP04vJOC5pnH2V/M/BETAB4pojIZFkQ=",
      "timestamp": "1724344145109",
      "idtimestamp": "",
      "signed_tree_head": ""
    },
  }
}
```

#### Prove Event Inclusion
```sh
cat event.json | veracity \
    --data-url $DATATRAILS_URL/verifiabledata \
    --tenant=$PUBLIC_TENANT_ID \
    --loglevel=INFO \
    verify-included
```

Its that simple. Note that by default Veracity produces no output on success to enable simple build
system integration. By supplying `--loglevel=INFO` we get some insight into what the tool is doing:

```sh
...
verifying for tenant: tenant/6ea5cd00-c711-3649-6914-7b125928bbb4
verifying: 5772 2889 01917aeb9103048500 publicassets/046ad7b4-dc99-4f90-9511-d2fad2e72bed/events/fef3c753-52e5-406b-8e41-8a36a2cc4818
OK|5772 2889|[c46a47677b043602dba8a9d1db3215207d1e2f4bdbb19bc07592602fa745b3b7, 18b5d6be487dc0b87d14cb7a389a6cf936aab2427dd26c1b230653f692964f06, a68a7678739a2e00431c25bf3d810b4f417830c3a95cfc692e771d6d54e37fa6, 907c561fd157a5a022aa4e42807bfca082c54d98531831847ad5414a1ad2b492, 9dfeaef9e86d6b857170245ec4cfc5d98fea11bba3937e211d134ab548eb743e, 04602adc424529275ce3415d55f31413743b67bf7e7fae03c90b08f1f5422264]
```
{{< note >}}
##### Detecting Tampering
Try tampering with `event.json` and re-running `verify-inclusion` to observe the failure:

```sh
sed "s/Business Critical Action/Malicious Action/g" event.json | \
    ./veracity \
    --data-url $DATATRAILS_URL/verifiabledata \
    --tenant=$PUBLIC_TENANT_ID \
    --loglevel=INFO \
    verify-included
```

```sh
...
verifying for tenant: tenant/6ea5cd00-c711-3649-6914-7b125928bbb4
verifying: 5772 2889 01917aeb9103048500 publicassets/046ad7b4-dc99-4f90-9511-d2fad2e72bed/events/fef3c753-52e5-406b-8e41-8a36a2cc4818
XX|5772 2889

error: the entry is not in the log. for tenant tenant/6ea5cd00-c711-3649-6914-7b125928bbb4
the entry is not in the log. for tenant tenant/6ea5cd00-c711-3649-6914-7b125928bbb4
```
{{< /note >}}

#### Offline Verification
Veracity can be used to verify the inclusion of an event in an offline backup of a DataTrails 
merkle log. We can do this by supplying a `--data-local` argument instead of `--data-url`. First, 
we'll need to download a copy of that log.

{{< note >}}
**Note:** Massifs are how DataTrails break the merkle log down into manageable chunks that record
up to a fixed number of events. Once that limit is reached, a new massif is started. `--data-local`
accepts a single massif file or a directory. The event we're verifying is contained by the first 
massif.
{{< /note >}}

```sh
curl -H "x-ms-blob-type: BlockBlob" -H "x-ms-version: 2019-12-12" https://app.datatrails.ai/verifiabledata/merklelogs/v1/mmrs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifs/0000000000000000.log -o mmr.log
```

We can now run the `verify-included` command again using our local log data and the output will be
the same.

```sh
cat event.json | \
    ./veracity \
    --data-local mmr.log \
    --tenant=$PUBLIC_TENANT_ID \
    --loglevel=INFO \
    verify-included
```

{{< note >}}
**Note:** Proof paths shown in the output were complete at time of writing. As the log grows the
proof path increases in length. See [this article](https://docs.datatrails.ai/developers/developer-patterns/navigating-merklelogs/) for a deep-dive into our merkle log.
{{< /note >}}

```sh
verifying for tenant: tenant/6ea5cd00-c711-3649-6914-7b125928bbb4
verifying: 5772 2889 01917aeb9103048500 publicassets/046ad7b4-dc99-4f90-9511-d2fad2e72bed/events/fef3c753-52e5-406b-8e41-8a36a2cc4818
OK|5772 2889|[c46a47677b043602dba8a9d1db3215207d1e2f4bdbb19bc07592602fa745b3b7, 18b5d6be487dc0b87d14cb7a389a6cf936aab2427dd26c1b230653f692964f06, a68a7678739a2e00431c25bf3d810b4f417830c3a95cfc692e771d6d54e37fa6, 907c561fd157a5a022aa4e42807bfca082c54d98531831847ad5414a1ad2b492, 9dfeaef9e86d6b857170245ec4cfc5d98fea11bba3937e211d134ab548eb743e, 04602adc424529275ce3415d55f31413743b67bf7e7fae03c90b08f1f5422264]
```

## Exploring the Merkle Log

Coming soon ...

## Further Reading

Coming soon ...

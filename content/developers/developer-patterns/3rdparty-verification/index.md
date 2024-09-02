---
title: "3rd party merkle log verification"
description: "Supporting 3rd party verification your DataTrails merkle log"
lead: "You don't have to trust DataTrails, easily maintain a verified replica of your merkle log"
date: 2024-08-22T19:35:35+01:00
lastmod: 2024-08-22T19:35:35+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 38
toc: true
aliases: 
  - /docs/developer-patterns/3rdparty-verification/

---

## Overview

The DataTrails ledger is a log that can be distributed.

When a replicated copy of your merkle log is held by an independent party,
it is impossible for DataTrails to modify your log to refute your claims.

By maintaining an indpendent log replica, in part or in whole, two key benefits are realized:

1. Detection of tampering: That it is instantly apparent if DataTrails removes or
changes the attestation to an event in a log.
1. Independence of proof: That after detecting a tamper, you are still able to
prove "who said what when", given your knowlege of the event and your replicated
section of the log.

To get these benefits, a full replica is not necessary. DataTrails provides a merkle log for each tenant.
Only the portions of the logs that attest to records that are still of interest
need be retained. And only for the specific tenants of interest.

All log replicas are equaly trustworthy. All log replicas accompanied by a
'seal' from DataTrails are irrefutable by DataTrails.
With a full replica, a full-audit possible, where regular data corruption is
detected, in either the replica or the original DataTrails copy.

## Environment Configuration for veracity

See [this article](/developers/developer-patterns/veracity/) for a general introduction to the `veracity` tool

The `veracity replicate-logs` command provides a convenient and reliable way to
create and maintain merkle log replicas for multiple tenants.

We will re-use the configuration from that article

```bash
# DataTrails Public Tenant
export PUBLIC_TENANT="6ea5cd00-c711-3649-6914-7b125928bbb4"

# Synsation Demo Tenant
# Replace to view your Tenant logs ane events
export TENANT="6a009b40-eb55-4159-81f0-69024f89f53c"
```

To view *your* protected events, replace `TENANT` with your `Tenant ID`.

## Replicating your first massif

To get a sense of how the basic commands work, in this example we ilustrate how
to find a log, *any* log, that has grown, and then replicate the section of that
log that the new records were added to. 


### First, find a tenant whose log has changed

This command will describe the activity for all tenants that have recently added events to their merkle log:

{{< tabs >}}
   {{< tab name="bash" >}}

   ```bash
   veracity watch -z 1h --mode tenants
   ```

   This will generate output similar to:
   ```output
   [
     {
       "massifindex": 0,
       "tenant": "6a009b40-eb55-4159-81f0-69024f89f53c",
       "idcommitted": "019176f5796d068500",
       "idconfirmed": "019176f5796d068500",
       "lastmodified": "2024-08-21T22:01:24Z",
       "massif": "v1/mmrs/tenant/6a009b40-eb55-4159-81f0-69024f89f53c/0/massifs/0000000000000000.log",
       "seal": "v1/mmrs/tenant/6a009b40-eb55-4159-81f0-69024f89f53c/0/massifseals/0000000000000000.sth"
     }
   ]
   ```
   There may be more than one entry listed, just pick any.
  {{< /tab >}}
{{< /tabs >}}

{{< note>}} If you get `error: no changes found` make the horizon bigger.{{< /note >}}

You can get output for a specific tenant using the `-t` (`--tenant`) option:

`veracity watch -z 10000h --mode tenants  -t $TENANT`


The `-t` option supports a comma delimited list of tenant identities.

Various human friendly forms are possible `-z 1s` would be activity in the last second, `-z 1m` the last minute.


## Using veracity to detect tamper

## Using veracity to achieve indpendence of proof

Same as Off line verification of the event

## Example automation using github action


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

This article provides the information needed to address three scenarios:

1. You want to detect if DataTrails improperly updates the log, and prove that to others.
2. You want to be able to produce proof that an event is in your log after DataTrails has improperly updated their copy.
3. You want fully independent verification of your events, without recourse to DataTrails.

Each of these can be accomplished using the veracity `replicate-logs` and
`watch` commands to check the log operation and replicate some or all of your
log data.

To get the benefits implied by these scenarios, a full replica is not necessary.
DataTrails provides a merkle log for each tenant.
Only the portions of the logs that attest to records that are still of interest need be retained.
And only for the specific tenants of interest.

The first two points require replication and verification of at least the most recently updated log section.

The second point requires retention of the local log sections verifying any event that is still of value.

The last point, full independent *verification*,
requires retention of the verifiable log data and the ability to reproduce the original event.

Because you have a trusted local copy of the verifiable data, even after you
detect a tamper, you can chose to rely on DataTrails storage of your event.

When you fetch the event, if it can be verified against your local log data, you
know that the DataTrails database remains correct, despite the impoperly updated
log. If it does not, you know that both the DataTrails database and your tenants
merkle log have been improperly updated. However, at this point, you can only
verify your event if you can reproduce the event independently.

All parties you have shared that event data with are also able to
replicate and verify its inclusion in both your log and theirs.


All log replicas are equaly trustworthy. All log replicas accompanied by a
'seal' from DataTrails are irrefutable by DataTrails.
With a full replica, a full-audit possible, where regular data corruption is
detected, in either the replica or the original DataTrails copy.

In this remainder of this article we provide examples covering how to use the
`veracity` tool to achieve these ends.

See [this article](/developers/developer-patterns/veracity/) for a general introduction to the `veracity` tool

## Environment Configuration for veracity

The `veracity replicate-logs` command provides a convenient and reliable way to
create and maintain merkle log replicas for multiple tenants.

We will use the following configuration

```bash
# DataTrails Public Tenant
export PUBLIC_TENANT="tenant/6ea5cd00-c711-3649-6914-7b125928bbb4"

# Synsation Demo Tenant
# Replace to view your Tenant logs ane events
export TENANT="tenant/6a009b40-eb55-4159-81f0-69024f89f53c"
```

To view *your* protected events, replace `TENANT` with your `Tenant ID`.

## Replicating the log for the public tenant

To get a sense of how `replicate-logs` works we replicate the public tenant's log


### Use replicate-logs to create a local, verified, replica of the DataTrails public tenant log

{{< tabs >}}
   {{< tab name="bash" >}}

   ```bash
   veracity --data-url https://app.datatrails.ai/verifiabledata \
       --tenant $PUBLIC_TENANT \
       replicate-logs --massif 0 \
       --replicadir merklelogs
   
   find merklelogs -type f
   ```
   
   This will generate output similar to
   
   ```
   merklelogs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifs/0000000000000000.log
   merklelogs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifseals/0000000000000000.sth
   ```
  {{< /tab >}}
{{< /tabs >}}

By default, all massifs up to and including the massif specified by `--massif
<N>` are verified remotely and checked for consistency against the local
replica. At the time of writing, the production public tenant is only on the first massif.

## Finding tenants with log additions

This command will describe the activity for all tenants that have recently added events to their merkle log:

{{< tabs >}}
   {{< tab name="bash" >}}

   ```bash
   veracity watch
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

   If instead you get

   ```
   error: no changes found
   ```

   It means there has been no activity in any tenant for the default watch horizon (how far back we look for changes)

   To set an explicit, and in this example very large, horizon try the following

   ```bash
   veracity watch --horizon 10000h
   ```


  {{< /tab >}}
{{< /tabs >}}

## Replicating the logs for the tenants with activity

To automatically replicate the logs that changes are detected for pipe the output of `watch` into `replicate-logs`

{{< tabs >}}
   {{< tab name="bash" >}}

   ```bash
   veracity watch \
   | veracity \
       replicate-logs --replicadir merklelogs
   ```

   This will replicate the logs for all tenants that have been active in the default time horizon

  {{< /tab >}}
{{< /tabs >}}


{{< note>}} Take care with larger time horizons, you may run into issues with rate limiting.{{< /note >}}

## Replicating just the latest changes to your log

By default, your full tenant log is replicated. The storage requirements are
roughly 4mb per massif. And each massif has the verification data for about 16000 events.

In many scenarios, you can achieve independent verifiability just by replicating
the most recently extended massif.

This is always suficient to detect a tamper. Provided you have 

When a tamper or inconistency is detected you most recently verifie log data will not be changed.



It's not necessary to keep a full replica of your log, if you are only interested in more recent items.

## Protections 


Detect that datatrails
veracity --ancestors 0

To detect if datatrails have improperly updated your log, y

## Using veracity to detect tamper

## Using veracity to achieve indpendence of proof

Same as Off line verification of the event

## Example automation using github action


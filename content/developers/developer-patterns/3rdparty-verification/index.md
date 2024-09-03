---
title: "3rd party merkle log verification"
description: "Supporting 3rd party verification a DataTrails merkle log"
lead: "You don't have to trust DataTrails by easily maintaining a verified replica of a merkle log"
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
When a replicated copy of a merkle log is held by an independent party, it is impossible for DataTrails to modify a log to refute claims.

A full replica is not necessary in many cases.
DataTrails provides a merkle log for each tenant.
Only the portions of the logs that attest to records that are still of interest need be retained.
And only for the specific tenants of interest.

This article provides the information needed to address three scenarios:

1. Detect if DataTrails improperly updates the log, and prove that to others
1. Be able to produce proof that an event is in a log after DataTrails has improperly updated their copy
1. Full independent verification of events, without recourse to DataTrails

Each of these can be accomplished using the veracity `replicate-logs` and `watch` commands to check the log operation and replicate some or all of log data.

The first two goals require replication and verification of at least the most recently updated log section.
The second goal requires retention of the local log sections verifying any event that is still of value.
The last goal, full independent *verification*, requires retention of the verifiable log data and the ability to reproduce the original event.

With a trusted local copy of the verifiable data, even after you detect a tamper, you can chose to rely on DataTrails storage of your event.

When the event is fetched, if it can be verified against local log data, knowing that the DataTrails log remains correct.
If it does not, know that both the DataTrails log and a tenants merkle log have been improperly updated.
However, you can only verify the event if the event can be reproduced independently.

All parties that have shared that event data are also able to replicate and verify the event inclusion in all copies of the log.

All log replicas are equally trustworthy.
All log replicas accompanied by a 'seal' from DataTrails are irrefutable by DataTrails.
With a full replica, a full-audit is possible, where regular data corruption is detected, in either the replica or the original DataTrails copy.

In this remainder of this article examples provide how to use `veracity` to achieve these goals.

See [Independently verifying DataTrails transparent merkle logs](/developers/developer-patterns/veracity/) for a general introduction to `veracity`.

## Environment Configuration for Veracity

The `veracity replicate-logs` command provides a convenient and reliable way to create and maintain merkle log replicas for multiple tenants.

Use the following configuration:

```bash
# DataTrails Public Tenant
export PUBLIC_TENANT="tenant/6ea5cd00-c711-3649-6914-7b125928bbb4"

# Synsation Demo Tenant
# Replace TENANT with your Tenant ID to view your Tenant logs and events
export TENANT="tenant/6a009b40-eb55-4159-81f0-69024f89f53c"
```

## Replicating the Log for the Public Tenant

To get a sense of how `replicate-logs` works replicate the public tenant's log

- Use Replicate-Logs to Create a Local, Verified, Replica of the Datatrails Public Tenant Log

  {{< tabs >}}
    {{< tab name="bash" >}}

  ```bash
  veracity --data-url https://app.datatrails.ai/verifiabledata \
      --tenant $PUBLIC_TENANT \
      replicate-logs --massif 0 \
      --replicadir merklelogs

  find merklelogs -type f
  ```

  Generates output similar to:

  ```output
  merklelogs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifs/0000000000000000.log
  merklelogs/tenant/6ea5cd00-c711-3649-6914-7b125928bbb4/0/massifseals/0000000000000000.sth
  ```

    {{< /tab >}}
  {{< /tabs >}}

By default, all massifs up to and including the massif specified by `--massif <N>` are verified remotely and checked for consistency against the local replica.
At the time of writing, the production public tenant is only on the first massif.

## Finding Tenants With Log Additions

`veracity watch` will describe the activity for all tenants that have been recently added events to their merkle log:

{{< tabs >}}
   {{< tab name="bash" >}}

  ```bash
  veracity watch
  ```

  Generates output similar to:

  ```json
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

  If instead you get:

  ```output
  error: no changes found
  ```

   There has been no activity in any tenant for the default watch horizon (how far back we look for changes).

   To set an explicit, and in this example very large, horizon try the following:

   ```bash
   veracity watch --horizon 10000h
   ```

  {{< /tab >}}
{{< /tabs >}}

## Replicating the Logs for the Tenants With Activity

To automatically replicate the logs that changes are detected for, pipe the output of `watch` into `replicate-logs`

- Replicate the logs for all tenants that have been active in the default time horizon

  {{< tabs >}}
    {{< tab name="bash" >}}

  ```bash
  veracity watch | \
    veracity \
    replicate-logs --replicadir merklelogs
  ```

    {{< /tab >}}
  {{< /tabs >}}

{{< note>}} Take care with larger time horizons, it may trigger issues with rate limiting.{{< /note >}}

## Replicating Just the Latest Changes to Your Log

By default, a full tenant log is replicated.
The storage requirements are roughly 4mb per massif, and each massif has the verification data for about 16000 events.

In many scenarios, independent verification can be achieved by replicating the most recently extended massif.

This is always sufficient to detect a tamper.
When a tamper or inconsistency is detected the most recently verified log data will not be changed.

It's not necessary to keep a full replica of a log, if only interested in more recent items.

## Protections

Detect that datatrails
veracity --ancestors 0

To detect if datatrails have improperly updated your log, y

## Using Veracity to Detect Tamper

## Using Veracity to Achieve Independence of Proof

Same as Off line verification of the event

## Example Automation Using Github Action

TBD

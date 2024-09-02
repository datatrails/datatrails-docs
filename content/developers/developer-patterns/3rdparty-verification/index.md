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


## Veracity replicate-logs

See [this article](/developers/developer-patterns/veracity/) for a general introduction to the `veracity` tool

The `veracity replicate-logs` command provides a convenient and reliable way to
create and maintain merkle log replicas for multiple tenants.

## Using veracity to detect tamper

## Using veracity to achieve indpendence of proof

Same as Off line verification of the event

## Example automation using github action


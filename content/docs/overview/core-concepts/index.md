---
title: "Core Concepts"
description: "RKVST Core Concepts"
lead: "RKVST Core Concepts"
date: 2021-06-14T10:57:58+01:00
lastmod: 2021-06-14T10:57:58+01:00
draft: false
images: []
menu: 
  docs:
    parent: "overview"
weight: 3
toc: true
---

## Assets

Central to all RKVST operations are _Assets_. These are the records that represent the collective 'Golden Thread' of evidence contributed by all stakeholders about a particular thing. Assets can represent anything: a physical object; a smart device; or even a business process. As long as shared accountability needs to be traced and trustworthy it can be recorded as an RKVST Asset.

RKVST Assets are essentially very simple: a collection of *attributes* that describe the Asset expressed as a standard JSON document. The power of the system comes from the fact that those attributes come with complete traceable provenance and are guaranteed to appear the same to every stakeholder, creating a single source of truth for shared business processes.

RKVST is not opinionated about Asset content meaning that Attributes can trace anything deemed important to participants. Much like #hashtags on Twitter they can be invented by anyone at any time, but once an Attribute has been seen once it will be fully traced from that point on.

A simple Asset might look like this:

```json
   {
      // Fixed global identity for this Asset
      "identity": "assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",

      // The set of tracked and traced attributes
      "attributes": {
        // arc_* are understood and processed by RKVST
        "arc_display_type": "Top Trump",
        "arc_display_name": "Opel Kadett Rallye 1900",
        "arc_description": "Opel Kadett Rallye 1900 Top Trump card",
        "arc_serial_number": "5a",
        "arc_home_location_identity": "locations/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",

        // arc_attachments is a collection of BLOBs attached to the Asset
        "arc_attachments": [
          {
            "arc_display_name": "arc_primary_image",
            "arc_hash_alg": "SHA256",
            "arc_hash_value": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "arc_attachment_identity": "blobs/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
          }
        ],
        
        // All others are user-defined attributes
        "bhp": "145",
        "top_speed": "190",
        "weight": "860",
        "engine_capacity": "1980"
      },

      // Behaviours define the set of APIs that can be used to interact with the Asset
      "behaviours": [
        "RecordEvidence"
      ],

      // Date and time at which these attributes were contemporary
      "at_time": "2021-06-25T12:40:03Z",

      // Storage and integrity properties - managed by the system
      "confirmation_status": "CONFIRMED",
      "tracked": "TRACKED",
      "owner": "0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "storage_integrity": "LEDGER"
    }
```

{{< note >}}
**Note:** The Asset Identity is fixed and constant for the life of the Asset and across all stakeholders. This ensures easy traceability and assurance that all stakeholders are collaborating on the same object and see the same complete history of Events.
{{< /note >}}

### Deleting Assets

An essential value of storing evidence in RKVST is that data is always available to stakeholders and cannot be shredded or manipulated later. Given this, it is not possible to actually delete Assets from the system, but there will be cases where it is desirable to hide assets in the UI or omit them from searches or compliance queries (for instance as a result of decommissioning or disposal of the corresponding physical asset).

To accommodate this need RKVST separates the Asset estate into 2 classes: tracked Assets (those that are interesting to the system and actively recording events); and untracked Assets (those that are no longer actively interesting). When for any reason it becomes desirable to remove an Asset the Asset Owner can make it _untracked_ so that it does not appear in lists or searches. 

{{< caution >}}
**Caution:** Untracking an Asset does not remove it or its Event history from the system; all stakeholders who previously had access to the record will continue to have access to the Event history, _including_ the untracking event, if they look for it.
{{< /caution >}}

For more detailed information on Assets and how to implement them, please refer to [the Assets API Reference](../../api-reference/assets-api/).

## Events

Any interaction with a device can be significant: from user logins to unexpected restarts or ad-hoc observations. Keeping a record of these events can build up a picture of how an asset came to be in its current state and provide crucial insight to future maintenance staff, auditors, and security remediation teams.

Knowing the current state of an Asset isn't enough: sure, it has software version 3.0 now but when was that installed? Before the major incident? After the major incident? This morning before the support call?

RKVST ensures complete and tamper-proof lineage and provenance for all Asset attributes by enforcing a simple rule:
**The only way to change an Asset attribute is through an Event that records Who Did What When to make that change.**

### Timestamps on Events

Lifecycle events in RKVST give stakeholders a shared view of “Who did What When to an Asset". The “What” and the "Asset" are quite straightforward, but the “When” and “Who” can be more nuanced.

Once committed to the RKVST system, each lifecycle event record carries 3 separate timestamps:
* `timestamp_declared` - an optional user-supplied value that tells when an event happened. This is useful for cases where the client system is off-line for a period but the user still wishes to record the accurate time and order of activities (eg inspection rounds in an air-gapped facility). If unspecified, the system sets timestamp_declared equal to timestamp_accepted (see below).
* `timestamp_accepted` - the time the event was actually received on the RKVST REST interface. Set by the system, cannot be changed by the client.
* `timestamp_committed` - the time the event was confirmed distributed to all DLT nodes in the value chain. Set by the system, cannot be changed by the client.

Having these 3 fields enables users of RKVST to accurately reflect what is claimed, whilst also preventing tampering and backdating of entries.

### User Principals on Events

Just as with the "When", the "Who" of “Who Did What When to an Asset" is potentially complicated if, for example, an application or gateway is acting on behalf of some other real-world user.

Once committed to the RKVST system, each lifecycle event record carries 2 separate user identities:
* `principal_declared` - an optional user-supplied value that tells who performed an event. This is useful for cases where the user principal/ credential used to authorize the Event does not accurately or usefully reflect the real-world agent (eg a multi-user application with device-based credentials).
* `principal_accepted` - the actual user principal information belonging to the credential used to access the RKVST REST interface. Set by the system and retrieved from the authorizing IDP, cannot be changed by the client.

For more detailed information on Assets and how to implement them, please refer to [the Events API Reference](../../api-reference/events-api/).

## Access Policies

Sharing the right amount of information with your value chain partners is critical to creating a trustworthy shared history for Assets. It is important that every participant be able to see and contribute to the management of Assets without compromising security, commercial, or private personal information. For example, competing vendors should not see each other’s information, but both should be able to freely collaborate with their mutual customer or industry regulator.

In other scenarios, it is desirable to share basic maintenance information with a vendor or external maintenance company, whilst restricting critical operating information such as run cycles and cyber SLAs to a much smaller group.

RKVST Access Policies are the method through which this access is defined, allowing Asset owners to collaborate with just the right partners at the right time, sharing as much or as little access to Assets as the needs of the value chain partners dictate. All transactions are private by default, meaning that only the asset owner can see and update asset histories until a sharing policy has been set up. This ensures ready compliance with important regimes such as GDPR and antitrust regulations, as well as allowing safe and ready collaboration with a large and diverse range of value chain partners in the RKVST network when required.

{{< note >}}
**Note:** To collaborate with a value chain partner you first need to enroll them as a partner in your RKVST tenancy by exchanging your RKVST public Subject Identity with each other, a little like making a new LinkedIn connection or Facebook friend.

This one-time manual process helps to underpin trust and security in your RKVST Access Policies by ensuring that the partners represented in them are the ones you expect.
{{< /note >}}

### Considerations

As with any system handling large amounts of important data, one must carefully consider the design and scope of Access Policy rules in RKVST.
Every situation is different, and the RKVST Access Policy system is flexible and powerful enough to support most situations, but in general it is recommended to follow some basic rules:
* Aim for fewest possible number of policies: This makes it much easier to review and manage access rights.
* Balance complex, highly-specific policies with simple, broad ones: Remember rights granted by policy are additive.
* A single Access Policy can contain several Permission Groups, so it is possible to define a single filter to cover a particular population of assets, then apply different rights to different sets of users and partner organizations. This is often a simpler way to manage access than to create separate Access Policies for each set of users.
* Remember attributes can change: ABAC policies are applied at time of access request, not at time of creation, so changing attributes on an asset may change which access policies apply to it. This is one of the primary advantages to an ABAC system but still needs to be borne in mind when designing access control processes.

### Access Policy configuration

RKVST employs a principle called Attribute-Based Access Control (ABAC) for users within an organization, and a related concept called Organization-Based Access Control (OBAC) to mediate data sharing between value chain participants.

Rather than applying a specific fixed policy to each asset, or grouping them into rigid hierarchies, Access Policies are defined in terms of the observable properties (or attributes) of Assets and users, and if both match, the policy is applied. This enables much greater flexibility and expressivity than traditional hierarchical or role-based methods, whilst at the same time reducing complexity in defining sharing in large-scale systems. 

RKVST Access Policies comprise 2 main parts:
* Filters: A list of attributes to match on Assets (this defines the scope of the Policy)
* Access Permissions: A list of access rights to be granted to users on those matching Assets

A simple access policy may look like this:

```json

    {
      // identity and tenant are non-modifiable system info
      "identity": "access_policies/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "tenant": "tenant/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",

      // User-friendly identifiers
      "display_name": "Sample Policy",
      "description": "An Access Policy created for RKVST user docs"

      // Filters define which Assets this Policy applies to
      "filters": [
        {
          // Any Crate, Box, or Bag ...
          "or": [
            "attributes.arc_display_type=Crate",
            "attributes.arc_display_type=Box",
            "attributes.arc_display_type=Bag"
          ]
        },
        {
          // ... whose registered handler is either Fred or Margaret
          "or": [
            "attributes.handler=Fred",
            "attributes.handler=Margaret"
          ]
        }
      ],

      // Permissions define what can be done with the matching Assets
      "access_permissions": [
        {
          // Grant access to partner organizations by Subject Identity
          "subjects": [
            // The Subject Identity for a known partner eg ACME Co
            "subjects/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" 
          ],

          // Grant access to local users by attribute (eg email address)
          "user_attributes": [ 
            { "or": [ "email=bill@synsation.com" ] } 
          ],
          
          // Limit the APIs they can call
          "behaviours": [ "RecordEvidence" ],
          
          // Select which Asset attributes these users can see
          "asset_attributes_read": [
            "Height",
            "arc_display_name",
            "arc_display_type"
          ],

          // Select which Asset attributes these users can modify
          "asset_attributes_write": [
            "Height"
          ],

          // Select which Events from the Asset history these users can see
          "event_arc_display_type_read": [
            "Measure",
            "Open",
            "Seal"
          ],

          // Select which Events these users can contribute to the history
          "event_arc_display_type_write": [
            "Measure"
          ],

          // Note the include_attributes field is deprecated
          "include_attributes": []
        }
      ]
    }
```

{{< note >}}
**Note:** Observe that there are 2 lists in the `filters` which concern different attributes. The effect of this is to say that an Asset matches the filters if it matches _at least one_ entry from _every list_. Or in other words, inner lists are OR, while outer lists are AND. 

For example:

```json
Filters = [
  { "or": [type=Pump, type=Valve] },
  { "or": [vendor=SynsationIndustries] },
  { "or": [location=ChicagoWest,location=ChicagoEast] }
]
```

In the above simplified example, the policy would apply to any Pump or Valve from SynsationIndustries installed in either the ChicagoWest or ChicagoEast sites, but it would not match:
* Other device types from SynsationIndustries;
* Pumps or Valves from any other vendor;
* SynsationIndustries Valves installed in a different location
{{< /note >}}

### Revoking Access

RKVST adopts a ‘default deny’ approach so access to an Asset Record is only possible if an Access Policy explicitly allows it.

Revoking access can therefore be achieved in a number of ways, any of which may be more or less appropriate for the circumstances:
* Remove the whole Access Policy
* Change the attributes of the Asset so that it no longer matches the Access Policy (eg change location)
* Change the attributes of the user or Subject so that they no longer match the Access Policy (eg change IDP group)
* Turn off the user’s login at the IDP

{{< note >}}
**Note:** As with any fair decentralized system it is not possible to 'unsee' information. Any change in OBAC access policies _including revoking OBAC access to a value chain partner_ only applies to new information contributed _after_ the policy change. This ensures continued fair access to the historic evidence base for all legitimate participants whilst also maintaining control of future operations with the Asset owner.
{{< /note >}}

## Attachments

Attachments in RKVST enable images, PDFs and other binary data to be attached to Assets and Events. This brings added richness to the evidence base and facilitates high fidelity collaboration between stakeholders.

### Attachments on Assets

Adding an attachment to an asset enables recording of characteristics of the asset that are very difficult to capture in the rigid structured data of asset attributes. For example, a device’s rating plate or latest service manual. While Asset Attachments are generally expected to be unique, the same Attachment can be applied to multiple assets, such as the case of a service manual PDF.

#### The Primary Image

Attachments on Assets are named in their arc_display_name property, so that they can be searched and indexed. Names are arbitrary and may be defined according to the needs of the application, but one name is reserved and interpreted by the RKVST services: `arc_primary_image`.
If an asset has an attachment named `arc_primary_image` then this will be used by the SaaS user interface and other tools to represent the asset.

### Attachments on Events

Adding an Attachment to an Event allows recording and communication of evidence that is difficult to capture in the rigid structured data of Event attributes. For example:
* a photograph of the physical state of a device such as alignment of components or wear on tamper seals at the time of a particular inspection.
* a PDF of a safety conformance report to support a maintenance event.
* a software manifest to support an update.
* an x-ray image.

To add Attachments to an Event simply specify an `arc_attachments` list in the `event_attributes` of the request when posting an event.

{{< note >}}
**Note:** Attachments cannot be searched or listed as a collection in their own right: they must always be associated with an Asset or Event and can only be downloaded by users with appropriate access rights to that Asset or Event.
{{< /note >}}

For more detailed information on Attachments and how to implement them, please refer to [the Blobs API Reference](../../api-reference/blobs-api/) and [the Attachments API Reference](../../api-reference/assets-api/)

## Locations

Assets in RKVST are arranged into locations, which allows virtual assets (eg digital twins) to be grouped together in a physical context (eg a single plant location). Locations have full 6-digit decimal latitude and longitude components allowing high-precision placement on any map renderer or GIS software you wish to link them to. It is not required for assets to be associated with a location, but it is a useful way to group assets in the same physical location and provides for numerous convenience functions in the RKVST UI.

This enables users of the system to quickly identify the answers to questions such as “how many PLCs in the Greyslake plant need to be updated?”, or “who was the last person to touch any device in the Cape Town facility?”. Locations support custom attributes which can be defined and used for any purpose by the user. This enables storage of a mailing address, phone number, or contact details of the site manager, for example.

{{< note >}}
**Note:** If your use case does not concern physical sites like factory plant locations or offices it is still possible to use Locations to logically group related Assets together. However it is likely to be more scalable to use a custom attribute to link them together.
{{< /note >}}

{{< caution >}}
**Caution:** It is important to recognize that the location does not necessarily denote the asset’s current position in space: it simply determines which facility the asset belongs to. For things that move around, GIS location information can be included with any event in the Asset Record in the `arc_gis_lat` and `arc_gis_lng` attributes, and the asset’s movement through space will be properly tracked.
{{< /caution >}}

## Compliance Policies

Trust is subjective. Compliance is a judgement call. No matter what security technology you have in play every trust decision you make will depend on the circumstances: who is accessing what; where they’re coming from; how sensitive an operation they’re attempting; the consequences of getting it wrong. An asset that is safe in one context may not be in another.

By maintaining a complete traceable record of Who Did What When to a Thing, RKVST makes it possible for any authorized stakeholder to quickly and easily verify that critical processes have been followed and recorded correctly.  And if they weren’t, the record makes it easy to discover where things went wrong and what to fix. For instance: missed or late maintenance rounds can be detected simply by spotting gaps in the maintenance record; cyber vulnerable devices can be found by comparing ideal baselines with patching records; out-of-order process execution and handling violations are visible to all; and back-dating is automatically detectable.

All of this is very valuable in audit and RCA situations after an incident, where there is time to collect together Asset Records, piece together the important parts, and analyse the meaning. 

But what if the same information could be used for real-time decision-making that might avert an incident? This is where RKVST’s “compliance posture” APIs come in. These take the thinking and processing burden off the client by providing a single, simple API call to answer the complex question: “given all you know about this asset, should I trust it right now?”. Additionally, and crucially for sensitive use cases, the yes or no answer comes with a detailed defensible reason why, which can be inspected by relevant stakeholders during or after the event.

When put all together, this enables high quality decision making based on the best available data, even giving confidence to automated or AI systems to play a full part in operations. Assets can be checked as part of access control logic, prior to accepting data or commands from them, prior to accepting a shipment, or anything else that is important to your business. Crucially, each stakeholder is able to define their own view on Compliance meaning they can each apply their own unique lens and business concerns to the same evidence base.

### Compliance policy configuration

In order to make these trust decisions, RKVST can be configured with Compliance Policies to check Assets against. These policies specify things like tolerance for vulnerability windows, maintenance SLAs, or detecting unusual values for attributes. For example:

* “Assets must be patched within 40 days of vulnerability notification”
* “Maintenance calls must be answered within 72 hours”
* "rad level must be less than"

Policies can also declare relative tolerances,  such as:

* "No shipping transfer should be more than 10% longer than the average time"
* "The reported weight of this container should be within 1 standard deviation of the historic mean"

Individual assets either pass or fail, and organizations can calculate their overall security/compliance posture based on what proportion of their assets are breaching their policy set. Compliance signals can also be used to identify where risk lies in an organization and help to prioritize remedial activities.

As with Assets and Events, Compliance Policies are very flexible and can be configured to answer a wide range of business problems. The following categories of policy are supported:

* *COMPLIANCE RICHNESS*: This Compliance Policy checks whether a specific attribute of an Asset is within acceptable bounds.<br><br>For example, "Weight attribute must be less than 1000 kg"
* *COMPLIANCE SINCE*: This Compliance Policy checks if the time since the last occurrence of a specific Event Type has elapsed a specified threshold.<br><br>For example, "Time since last Maintenance must be less than 72 hours"

* *COMPLIANCE CURRENT OUTSTANDING*: This Compliance Policy will only pass if there is an associated closing event addressing a specified outstanding event.<br><br>For example, checking there are no outstanding "Maintenance Request" Events that are not addressed by an associated "Maintenance Performed" Event.

* *COMPLIANCE_PERIOD_OUTSTANDING*: This Compliance Policy will only pass if the time between a pair of correlated events did not exceed the defined threshold.<br><br>For example, a policy checking that the time between "Maintenance Request" and  "Maintenance Performed" Events does not exceed the maximum 72 hours.

* *COMPLIANCE_DYNAMIC_TOLERANCE*: This Compliance Policy will only pass if the time between a pair of correlated events or the value of an attribute does not exceed the a variability from the usually observed values.<br><br>For example, a policy checking that maintenance times are not considerably longer than normal, or the weight of a container is not much less than the typical average.

{{< note >}}
**Note:** To correlate events define the attribute `arc_correlation_id` in the Event Attributes and set it to the same value on each pair of events that are to be associated.
{{< /note >}}

## Perspectives 

In the Asset example above there is an `at_time` property, which reflects a date and time at which these attributes and values were contemporary. Usually this will just be the current system time, but with RKVST it is possible to go back in time and ask the question "what would that asset have looked like to me had I looked at it last week/last year/before the incident?". Using its high integrity record of Asset lineage RKVST can give clear and faithful answers to those questions with no fear of backdating, forgery, or repudiation getting in the way.

To do this, simply add `at_time=TIMESTAMP` to your query. For example, to check the state an asset was in at 15:30 UTC on 23rd June:

```bash
curl -H "Authorization: Bearer $(cat .auth_token)" -H "Content-Type: application/json" https://app.rkvst.io/archivist/v2/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx?at_time=2021-06-23T15:30:00Z | jq 
```

Compliance calls can be similarly modified to answer questions like "had I asked this question at the time, what would the answer have been?" or "had the AI asked this question, would it have made a better decision?". This can be done by adding a `compliant_at` timestamp to the compliance request.

## That's it!

These are all the basics of RKVST. With this knowledge you can now [jump straight into the API](../../api-reference/) or [try RKVST Basics](../../rkvst-basics).

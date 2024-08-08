---
title: "Software Package Profile"
description: "Sharing and Distributing a Software Bill of Materials with DataTrails"
lead: "Sharing and Distributing a Software Bill of Materials with DataTrails"
date: 2023-06-26T11:56:01+01:00
lastmod: 2023-06-26T11:56:01:31+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 36
toc: true
---

## Overview

The DataTrails Software Package profile is a set of suggested Asset and Event attributes that enable the recording of an immutable and verifiable Software Bill of Materials (SBOM).

The [NTIA](https://www.ntia.gov/sites/default/files/publications/sbom_faq_-_20201116_0.pdf) describes a SBOM as "*a formal record containing the details and supply chain relationships of various components used in building software.*"

## Software Package Profile Asset Attributes

| NTIA Attribute      | Asset Attributes              | Meaning                                                                      | Requirement                 |
|---------------------|-------------------------------|------------------------------------------------------------------------------|-----------------------------|
| Author Name         | sbom_author                   | The name of the Package Author                                               | Required                    |
| Supplier Name       | sbom_supplier                 | The name of the Package Supplier                                             | Required                    |
| Component Name      | sbom_component,(arc_display_name if appropriate)| The name of the Software Package                           | Required                    |
| Version String      | sbom_version                  | The version of the Software Package                                          | Required                    |
| Unique Identifier   | sbom_uuid                     | A unique identifier for the Package, DataTrails provides a Unique ID per asset but it may be preferred to include an existing internal reference instead                             | Required                    |
| N/A                 | sbom_repo                     | Link to the Git Repo of the Component                                        | Optional                    |
| N/A                 | sbom_release_notes            | Link to the release notes of the package version                             | Optional                    |
| N/A                 | sbom_license                  | The licensing used by the component (if specified)                           | Optional                    |

{{< note >}}

**Note:** Software Package Profile Attribute Namespace

The `sbom_` prefix is used to designate attributes that are part of the profile. Some of these are interpreted by DataTrails and others are guidelines.
{{< /note >}}

### Public SBOM

In the API, you must express `public` as an asset attribute and have `true` as a property to make an SBOM public. The default is 'false'.
In the UI this is done by setting `Attest Publicly` to `On`.

{{< tabs name="create_sbom_public" >}}
{{{< tab name="UI" >}}
Select `Assets & Documents` from the sidebar and then `Add Custom Asset`. Fill in the desired details.
Set the `Attest Publicly` toggle to `On`.

{{< img src="PublicCheck.png" alt="Rectangle" caption="<em>Check Asset as Public</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
Create a YAML file with your desired Asset details. Set keyword `public` to true.

```yaml
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create an asset.
      asset_label: Publicly Attested Asset 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
    public: true
    attributes: 
      arc_display_name: Publicly Attested Asset 
      arc_display_type: Example
      arc_description: This example asset is publicly attested, so anyone with the link can access its details without signing in to DataTrails.
      some_custom_attribute: anything you like
    confirm: false
```

{{< /tab >}}
{{< tab name="JSON" >}}
Create a JSON file with your desired Asset details. Set keyword `public` to true.

```json
{
    "behaviours": ["RecordEvidence"],
    "attributes": {
        "arc_display_name": "Publicly Attested Asset",
        "arc_display_type": "Example",
        "arc_description": "This example asset is publicly attested, so anyone with the link can access its details without signing in to DataTrails."
    },
    "public": true
}
```

{{< /tab >}}
{{< /tabs >}}

## Software Package Profile Event Types and Attributes

### Release Event

A Release is the event used by a Supplier to provide an SBOM for their Software Package in DataTrails.

The Release attributes tracked in DataTrails should minimally represent the base information required by the NTIA standard and be recorded in two, separate, lists of attributes; **Asset Attributes** would track details about the latest release of the SBOM at the time of the event creation, the **Event Attributes** then track details about the release of the SBOM that is being submitted.

{{< note >}}

##### Release Event Attribute Namespace

The `sbom_` prefix is used to designate attributes that are part of the event and asset. Some of these are interpreted by DataTrails and others are guidelines
{{< /note >}}

| NTIA Attribute      | Event Attributes         | Meaning                                                                | Requirement                               |
|---------------------|--------------------------|------------------------------------------------------------------------|-------------------------------------------|
| N/A                 | arc_display_type         | Tells DataTrails how to interpret Event                                     | Required, must set to `Release` |
| Author Name         | sbom_author              | The name of the Package Author                                         | Required |
| Supplier Name       | sbom_supplier            | The name of the Package Author                                         | Required                    |
| Component Name      | sbom_component           | The name of the Package                                                | Required                            |
| Version String      | sbom_version             | The version of the Package                                             | Required |
| Unique Identifier   | sbom_uuid                | A unique identifier for the Package, DataTrails provides a Unique ID per asset but it may be preferred to include an existing internal reference instead                  | Required    |
| N/A                 | sbom_repo                | Link to the Git Repo of the Component                                  | Optional    |
| N/A                 | sbom_release_notes       | Link to the release notes of the release                               | Optional |
| N/A                 | sbom_license             | The licensing used by the component (if specified)                     | Optional |
| N/A                 | sbom_exception           | If included value is always `true`                                     | Optional |
| N/A                 | sbom_vuln_reference      | If this release resolves a specific vulnerability you can highlight a shared Vulnerability reference number(s) | Optional |

| NTIA Attribute      | Asset Attributes              | Meaning                                                                      | Requirement                 |
|---------------------|-------------------------------|------------------------------------------------------------------------------|-----------------------------|
| Author Name         | sbom_author                   | The name of the Package Author                                               | Required                    |
| Supplier Name       | sbom_supplier                 | The name of the Package Supplier                                             | Required                    |
| Component Name      | sbom_component,(arc_display_name if appropriate)| The name of the Software Package                           | Required                    |
| Version String      | sbom_version                  | The version of the Software Package                                          | Required                    |
| Unique Identifier   | sbom_uuid                     | A unique identifier for the Package, DataTrails provides a Unique ID per asset but it may be preferred to include an existing internal reference instead                             | Required                    |
| N/A                 | sbom_repo                     | Link to the Git Repo of the Component                                        | Optional                    |
| N/A                 | sbom_release_notes            | Link to the release notes of the package version                             | Optional                    |
| N/A                 | sbom_license                  | The licensing used by the component (if specified)                           | Optional                    |

{{< note >}}

##### Exception

When used in tandem with Release Plan and Accepted events the exception is a useful record of when an emergency has caused a release to be pushed without needing an initial approval or plan.
{{< /note >}}

### Release Plan and Release Accepted

Release events can be optionally enhanced by using ‘Release Plan’ and ‘Release Accepted’ events alongside them.

Release Plan events demonstrate an intent to introduce a new release, it should describe which version you want to release and who wants to release it. For example, it could include draft release notes explaining what is being updated and why it should be updated.

Release Accepted events demonstrate an approval on a Release Plan to go forward, it may be that the plan details a need to introduce a fix for a specific vulnerability and the security team is needed to sign off the release going forward.

These events are not essential to the process so can be omitted in a standard or minimal deployment but they are actively encouraged. As they should not affect the information about the latest Software Package Release there should be no Asset Attributes included, other NTIA attributes may also not be necessary or not available until release (e.g. Component Hash).

The Key Attribute that should be recorded is the version of the release that is being planned and accepted.

### Release Plan

{{< note >}}

##### Release Plan Event Attribute Namespace

The `sbom_planned_` prefix is used to designate attributes that are part of the event. Some of these are interpreted by DataTrails and others are guidelines.
{{< /note >}}

| NTIA Attribute      | Event Attributes         | Meaning                                         | Requirement                               |
|---------------------|--------------------------|-------------------------------------------------|-------------------------------------------|
| N/A                 | arc_display_type         | Tells DataTrails how to interpret Event              | Required, must set to `Release Plan` |
| Component Name      | sbom_planned_component   | The planned name of the Package                 | Required        |
| Version String      | sbom_planned_version     | The planned version of the Package              | Required |
| N/A                 | sbom_planned_reference   | A reference number for the plan (such as internal change request number)| Required |
| N/A                 | sbom_planned_date        | The planned release date                        | Required |
| N/A                 | sbom_planned_captain     | The planned Release Captain (a common term for someone who is responsible for performing a Release; someone like an Owner in Agile serves a different purpose but may also be used if appropriate). This is mandatory as it describes who should be responsible for the release  | Required |
| Author Name         | sbom_planned_author      | The planned name of the Package Author          | Optional |
| Supplier Name       | sbom_planned_supplier    | The planned name of the Package Supplier        | Optional |
| Component Hash      | sbom_planned_hash        | The planned hash of the component files/installation (per version)| Optional |
| Unique Identifier   | sbom_planned_uuid        | The planned unique identifier for the Package, DataTrails provides a Unique ID per asset but it may be preferred to include an existing internal reference instead              | Optional |
| N/A                 | sbom_planned_license     | If there is an intended change to the license this may be needed| Optional |
| N/A                 | sbom_planned_vuln_reference| If this release intends to resolve a specific vulnerability you can highlight a shared Vulnerability reference number(s)              | Optional |

### Release Accepted Event

{{< note >}}

##### Release Accepted Event Attribute Namespace

The `sbom_accepted_` prefix is used to designate attributes that are part of the event. Some of these are interpreted by DataTrails and others are guidelines.
{{< /note >}}

| NTIA Attribute      | Event Attributes                | Meaning                                         | Requirement                               |
|---------------------|---------------------------------|-------------------------------------------------|-------------------------------------------|
| N/A                 | arc_display_type                | Tells DataTrails how to interpret Event              | Required, must set to `Release Accepted` |
| Component Name      | sbom_accepted_component         | The accepted name of the Package                | Required        |
| Version String      | sbom_accepted_version           | The accepted version of the Package             | Required |
| N/A                 | sbom_accepted_reference         | The reference number of the associated plan     | Required |
| N/A                 | sbom_accepted_date              | The accepted release date                       | Required |
| N/A                 | sbom_accepted_captain           | The accepted Release Captain (a common term for someone who is responsible for performing a Release; someone like an Owner in Agile serves a different purpose but may also be used if appropriate). This is mandatory as it describes who should be responsible for the release         | Required |
| N/A                 | sbom_accepted_approver          | Describes who has accepted the plan             | Required |
| Author Name         | sbom_accepted_author            | The accepted name of the Package Author         | Optional |
| Supplier Name       | sbom_accepted_supplier          | The accepted name of the Package Supplier       | Optional |
| Component Hash      | sbom_accepted_hash              | The accepted hash of the component files/installation (per version)| Optional |
| Unique Identifier   | sbom_accepted_uuid              | The accepted unique identifier for the Package, DataTrails provides a Unique ID per asset but it may be preferred to include an existing internal reference instead              | Optional |
| N/A                 | sbom_accepted_vuln_reference    | If this release intends to resolve a specific vulnerability you can highlight a shared Vulnerability reference number(s)              | Optional |

### Patch Event

Patches are often supplied to customer in an Out-Of-Band procedure to address critical bugs or vulnerabilities, usually with a short-term turnaround that can be outside the normal release cadence.

It is typically expected a Patch should contain its own SBOM separate to the Primary SBOM.

{{< note >}}

##### Patch Event Attribute Namespace

The `sbom_patch_` prefix is used to designate attributes that are part of the event. Some of these are interpreted by DataTrails and others are guidelines.
{{< /note >}}

| NTIA Attribute      | Event Attributes         | Meaning                                         | Requirement                               |
|---------------------|--------------------------|-------------------------------------------------|-------------------------------------------|
| N/A                 | arc_display_type         | Tells DataTrails how to interpret Event              | Required, must set to `Patch`             |
| Component Name      | sbom_patch_target_component| The component the Patch targets               | Required                                  |
| Version String      | sbom_patch_version       | The version string of the Patch                 | Required                                  |
| Author Name         | sbom_patch_author        | The name of the Patch Author                    | Required                                  |
| Supplier Name       | sbom_patch_supplier      | The name of the Patch Supplier                  | Required                                  |
| Component Hash      | sbom_patch_hash          | The hash of the Patch files/installation (per version) | Required                           |
| Unique Identifier   | sbom_patch_uuid          | The accepted unique identifier for the Package, DataTrails provides a Unique ID per asset but it may be preferred to include an existing internal reference instead                | Required |
| N/A                 | sbom_patch_target_version| The version of the component the patch is targeted/built from | Required                    |
| N/A                 | sbom_patch_repo          | Link to the Git Repo/Fork/Branch of the Component (if different to the latest release repo) | Optional |
| N/A                 | sbom_patch_license       | The licensing used by the component (if specified and different to the latest release license) | Optional |
| N/A                 | sbom_patch_vuln_reference| If this patch resolves a specific vulnerability you can highlight a shared Vulnerability reference number | Optional |

### Vulnerability Disclosure and Update

These Event types are used for vulnerability management.
The first is to disclose knowledge of a vulnerability and the second is to update the status of the vulnerability after investigation is complete.

{{< note >}}

##### Vulnerability Disclosure Event Attribute Namespace

The `vuln_` prefix is used to designate attributes that are part of the event. All of these are interpreted by DataTrails.
{{< /note >}}

#### Vulnerability Disclosure

| Event Attributes         | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | Tells DataTrails how to interpret Event              | Required, must set to `Vulnerability Disclosure` |
| vuln_name                | Friendly Name for the Vulnerability             | Required        |
| vuln_reference           | Reference Number (e.g. internal tracking number), useful when there may be multiple updates to a vulnerability during an investigation and for referencing when a particular release is expected to solve a vulnerability | Required |
| vuln_id                  | Specific ID of Vulnerability (e.g CVE-2018-0171)| Required |
| vuln_category            | Type of Vulnerability (e.g. CVE)                | Required |
| vuln_severity            | Severity of Vulnerability (e.g. HIGH)           | Required |
| vuln_status              | Whether the Vulnerability actually affects your component or is being investigated (e.g Known_not_affected)| Required |
| vuln_author              | Author of Vulnerability Disclosure              | Required |
| vuln_target_component    | Affected Component                              | Required |
| vuln_target_version      | Affected Version(s)                             | Required |

#### Vulnerability Update

| Event Attributes         | Meaning                                         | Requirement                               |
|--------------------------|-------------------------------------------------|-------------------------------------------|
| arc_display_type         | Tells DataTrails how to interpret Event              | Required, must set to `Vulnerability Update` |
| vuln_name                | Friendly Name for the Vulnerability             | Required        |
| vuln_reference           | Reference Number (e.g. internal tracking number), useful when there may be multiple updates to a vulnerability during an investigation and for referencing when a particular release is expected to solve a vulnerability | Required |
| vuln_id                  | Specific ID of Vulnerability (e.g CVE-2018-0171)| Required |
| vuln_category            | Type of Vulnerability (e.g. CVE)                | Required |
| vuln_severity            | Severity of Vulnerability (e.g. HIGH)           | Required |
| vuln_status              | Whether the Vulnerability actually affects your component or is being investigated (e.g Known_not_affected)| Required |
| vuln_author              | Author of Vulnerability Disclosure              | Required |
| vuln_target_component    | Affected Component                              | Required |
| vuln_target_version      | Affected Version(s)                             | Required |

### EOL Event

{{< note >}}

##### EOL Event Attribute Namespace

The `sbom_eol_` prefix is used to designate attributes that are part of the event. All of these are interpreted by DataTrails.
{{< /note >}}

An event to mark the Package as End of Life.
| NTIA Attribute      | Event Attributes         | Meaning                                         | Requirement                               |
|---------------------|--------------------------|-------------------------------------------------|-------------------------------------------|
| N/A                 | arc_display_type         | Tells DataTrails how to interpret Event              | Required, must set to `EOL`               |
| Component Name      | sbom_eol_target_component| The component the EOL targets                   | Required                                  |
| Version String      | sbom_eol_target_version  | The version string affected by the EOL          | Required                                  |
| Author Name         | sbom_eol_author          | The name of the EOL Author                      | Required                                  |
| Unique Identifier   | sbom_eol_uuid            | The accepted unique identifier for the Package, DataTrails provides a Unique ID per asset but it may be preferred to include an existing internal reference instead                                  | Required |
| N/A                 | sbom_eol_target_date     | The date on which the EOL will be active         | Required                                 |

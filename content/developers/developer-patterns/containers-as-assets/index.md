---
title: "Containers as Assets"
description: "Using RKVST to Represent Containers"
lead: "Using RKVST to Represent Containers"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 32
toc: true
---

## Represent Containers Using RKVST

RKVST Assets can be used to track the status, contents, location, and other key attributes of containers over time. This can also be done for containers within containers. For example, you may wish to track bags inside boxes that are inside a shipping container being transported on a train.

## Create a Container Asset

Creating an Asset to represent a container is the same as creating any other asset. For more detail on this process, please see our [RKVST Basics guide](/platform/rkvst-basics/creating-an-asset/). For this example, we will create a simple asset that we will call `Shipping Container`. Note that with RKVST, we could also record more complex attributes such as size of the container, weight, location, or any other important details. For now, we will create a minimal Asset that includes the name and type.

{{< tabs name="shipping_container_asset" >}}
{{{< tab name="UI" >}}
{{< img src="ShippingContainer.png" alt="Rectangle" caption="<em>Create the Shipping Container</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `rkvst-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

```yaml 
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create a shipping container asset.
      asset_label: Shipping Container 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
    proof_mechanism: SIMPLE_HASH
    attributes: 
      arc_display_name: Shipping Container
      arc_display_type: Shipping Container
    confirm: true
```
{{< /tab >}}
{{< tab name="JSON" >}}

```json
{
    "behaviours": ["RecordEvidence", "Attachments"],
    "proof_mechanism": "SIMPLE_HASH",
    "attributes": {
        "arc_display_name": "Shipping Container",
        "arc_display_type": "Shipping Container",
    }
}
```
{{< /tab >}}}
{{< /tabs >}}

## Associate an Item or Container with Another Container

Now that we have created a `Shipping Container` Asset, we can create an Asset to represent an item or container within the Shipping Container. To do this, we will create another Asset and add a custom `Asset Attribute` that links it to our Shipping Container. For example, let's create an Asset to represent a box that is being transported within the Shipping Container. 

{{< note >}}
**Note:** For this example, we used the custom attribute `within_container`, but you could use any key to associate the Assets that does not contain the reserved 'arc_' prefix.
{{< /note >}}

{{< tabs name="box_asset" >}}
{{{< tab name="UI" >}}
{{< img src="BoxAsset.png" alt="Rectangle" caption="<em>Create the Box</em>" class="border-0" >}}

{{< img src="WithinContainer.png" alt="Rectangle" caption="<em>Add an Extended Attribute</em>" class="border-0" >}}

{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `rkvst-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

```yaml 
---
steps:
  - step:
      action: ASSETS_CREATE_IF_NOT_EXISTS
      description: Create a box asset and associate with Shipping Container.
      asset_label: Box 
    selector: 
      - attributes: 
        - arc_display_name
    behaviours: 
      - RecordEvidence
      - Attachments
    proof_mechanism: SIMPLE_HASH
    attributes: 
      arc_display_name: Box
      arc_display_type: Box
      within_container: Shipping Container
    confirm: true
```
{{< /tab >}}
{{< tab name="JSON" >}}

```json
{
    "behaviours": ["RecordEvidence", "Attachments"],
    "proof_mechanism": "SIMPLE_HASH",
    "attributes": {
        "arc_display_name": "Box",
        "arc_display_type": "Box",
        "within_container": "Shipping Container",
    }
}
```
{{< /tab >}}}
{{< /tabs >}}

It is now recorded that there is a `Box` within the container `Shipping Container`. We repeat this process to create another Asset and record what was inside the `Box`.

## List All Assets Asssociated with a Container

To retrieve all Assets associated with a container, you can run a query with a filter that will identify which Assets have the attribute `within_container` set to the desired value. To list all Assets inside of `Shipping Container`:

{{< tabs name="list_contents" >}}
{{{< tab name="UI" >}}
Go to the `Audit/Search` page and filter the Assets and Events within your tenancy.
{{< img src="AssetFilter.png" alt="Rectangle" caption="<em>Filter Assets and Events</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `rkvst-archivist` python package.

[Click here](https://python.rkvst.com/runner/index.html) for installation instructions.
{{< /note >}}

```yaml 
---
steps:
  - step:
      action: ASSETS_LIST
      description: List all assets within Shipping Container.
      print_response: true
    attrs:
      within_container: Shipping Container
```
{{< /tab >}}
{{< tab name="CURL" >}}
See instructions for [creating your `BEARER_TOKEN_FILE`](/platform/rkvst-basics/getting-access-tokens-using-app-registrations/) here.

```bash
curl -g -v -X GET \
     -H "@$BEARER_TOKEN_FILE" \
     "https://app.rkvst.io/archivist/v2/assets?attributes.within_container=Shipping%20Container"
```
{{< /tab >}}}
{{< /tabs >}}
---
title: "Containers as Assets"
description: "Using DataTrails to Represent Containers"
lead: "Using DataTrails to Represent Containers"
date: 2021-05-31T15:18:01+01:00
lastmod: 2021-05-31T15:18:01:31+01:00
draft: false
images: []
menu:
  developers:
    parent: "developer-patterns"
weight: 32
toc: true
aliases: 
  - /docs/developer-patterns/containers-as-assets/
---

## Represent Containers Using DataTrails

DataTrails Assets can be used to track the status, contents, location, and other key attributes of containers over time. This can also be done for containers within containers. For example, you may wish to track bags inside boxes that are inside a shipping container being transported on a train.

## Create a Container Asset

A Container Asset is not a special type of asset, it is a label that is given to an Asset that has been created to represent a container. For more detail on the Asset creation process, please see our [DataTrails Overview guide](/platform/overview/creating-an-asset/).<br>For this example, we will create a simple asset that we will call `Shipping Container`. Note that with DataTrails, we could also record more complex attributes such as size of the container, weight, location, or any other important details. For now, we will create a minimal Asset that includes the name and type.

{{< tabs name="shipping_container_asset" >}}
{{{< tab name="UI" >}}
{{< img src="ShippingContainer.png" alt="Rectangle" caption="<em>Create the Shipping Container</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.

[Click here](https://python.datatrails.ai/runner/index.html) for installation instructions.
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
    attributes: 
      arc_display_name: Shipping Container
      arc_display_type: Shipping Container
    confirm: false
```

{{< /tab >}}
{{< tab name="JSON" >}}

```json
cat > asset.json <<EOF
{
  "behaviours": ["RecordEvidence"],
  "attributes": {
      "arc_display_name": "Shipping Container",
      "arc_display_type": "Shipping Container"
  }
}
EOF
```

Use `curl` to `POST` the asset, viewing the result with `jq`:

```bash
curl -X POST \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     -H "Content-Type: application/json" \
     -d "@asset.json" \
     https://app.datatrails.ai/archivist/v2/assets | jq
```

If errors occur, see [Troubleshooting Token Generation](../getting-access-tokens-using-app-registrations/#troubleshooting-token-generation)
{{< /tab >}}}
{{< /tabs >}}

## Associate an Item or Container with Another Container

Now that we have created a `Shipping Container` Asset, we can create another Asset to represent an item or a box of items that are to be shipped in the Shipping Container. To do this, we will create another Asset and add a custom `Asset Attribute` that links it to our Shipping Container. For example, let's create an Asset to represent a box that is being transported within the Shipping Container.

{{< note >}}
**Note:** For this example, we used the custom attribute `within_container`, but you could use any key to associate the Assets that does not contain the reserved `arc_` prefix.
{{< /note >}}
{{< tabs name="box_asset" >}}
{{{< tab name="UI" >}}
</br>

1. Set the `Name` and `Type`  
    {{< img src="BoxAsset.png" alt="Rectangle" caption="<em>Create the Box</em>" class="border-0" >}}
1. Click `Advanced Options`  
    {{< img src="WithinContainer.png" alt="Rectangle" caption="<em>Add an Extended Attribute</em>" class="border-0" >}}
1. Click `ADD ATTRIBUTE` to set `Extended Attributes`
1. Add Attribute = `within_container` and Value = `Shipping Container`
1. Click `REGISTER ASSET` to complete the association of the box within the container
1. Repeat the above a few times, editing the `Name` to add several boxes within the `Shipping Container`
{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.

[Click here](https://python.datatrails.ai/runner/index.html) for installation instructions.
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
    attributes: 
      arc_display_name: Box-1
      arc_display_type: Box
      within_container: Shipping Container
    confirm: false
```

Repeat the above a few times, editing the `arc_display_name` to add several boxes within the `Shipping Container`
{{< /tab >}}
{{< tab name="JSON" >}}

```json
cat > asset-box.json <<EOF
{
    "behaviours": ["RecordEvidence"],
    "attributes": {
        "arc_display_name": "Box-1",
        "arc_display_type": "Box",
        "within_container": "Shipping Container"
    }
}
EOF
```

Use `curl` to `POST` the asset, viewing the result with `jq`:

```bash
curl -X POST \
     -H "@$HOME/.datatrails/bearer-token.txt" \
     -H "Content-Type: application/json" \
     -d "@asset-box.json" \
     https://app.datatrails.ai/archivist/v2/assets | jq
```

Repeat the above a few times, editing the `arc_display_name` to add several boxes within the `Shipping Container`

If errors occur, see [Troubleshooting Token Generation](../getting-access-tokens-using-app-registrations/#troubleshooting-token-generation)
{{< /tab >}}}
{{< /tabs >}}

The `Box(es)` have been recorded as being within the `Shipping Container`.

## List All Assets Associated With a Container

To retrieve all Assets associated with a container, you can run a query with a filter that will identify which Assets have the attribute `within_container` set to the desired value. To list all Assets inside of `Shipping Container`:

{{< tabs name="list_contents" >}}
{{{< tab name="UI" >}}
</br>

1. Select `Audit/Filter` in the navigation to filter Assets and Events within your tenancy
1. Select `ADD FILTER`
1. Select `Asset Attribute`, set the name to `within_container` and the value to `Shipping Container`
1. Select `APPLY FILTERS` to view the subset of Assets created  
    {{< img src="AssetFilter.png" alt="Rectangle" caption="<em>Filter Assets and Events</em>" class="border-0" >}}
{{< /tab >}}
{{< tab name="YAML" >}}
{{< note >}}
**Note:** To use the YAML Runner you will need to install the `datatrails-archivist` python package.

[Click here](https://python.datatrails.ai/runner/index.html) for installation instructions.
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

```bash
curl -g -X GET \
     -H "$HOME/.datatrails/bearer-token.txt" \
     "https://app.datatrails.ai/archivist/v2/assets?attributes.within_container=Shipping%20Container" | jq
```

{{< /tab >}}}
{{< /tabs >}}

---
title: "Tutorial"
description: ""
lead: ""
date: 2021-05-18T15:33:31+01:00
lastmod: 2021-05-18T15:33:31+01:00
draft: false
images: []
menu:
  docs:
    parent: "quickstart"
weight: 26
toc: true
---

## Creating an Asset

1. Using the Sidebar, select `Add Asset`.

{{< img src="AssetAddNT.png" alt="Rectangle" caption="<em>Adding an Asset</em>" class="border-0" >}}

2. You will see an Asset Creation form where you can provide details about your new Asset:

{{< img src="AssetCreateQS.png" alt="Rectangle" caption="<em>Creating an Asset</em>" class="border-0" >}}

3. At a minimum, you will need to add an Asset Name, Asset Type, and your choice of Proof Mechanism when using the UI to create an Asset:

* `Asset Name` - This is the unique name of the Asset i.e. 'My Bike'
* `Asset Type` - This is the type of Asset - while arbitrary, it is best to have consistency amongst the Assets you use i.e. if it is a bike, the type could be `Bike` which will then be pre-populated for future Assets to use.
* `Proof Mechanism` - This identifies how frequently Asset history information is committed to the blockchain. `Khipu` - or 'Transactional Immutability' - indicates that every Event is committed through smart contracts and immediately committed to the chain. `Simple Hash` - or 'Batched Immutability' - indicates that Events are processed in the RKVST tenancy and then periodically collected together and committed to the chain as a batch.

{{< img src="AssetCreationDetailsQS.png" alt="Rectangle" caption="<em>Adding Asset Details</em>" class="border-0" >}}

4. You may wish to add other details to your Asset, including Attachments and Extended Attributes. 

Extended Attributes are user-defined and added per unique Asset.

To add a new Attribute to an Asset select `Add Attribute` and then enter your key-value pair.

For Example:

{{< img src="AssetExtendedAttributesQS.png" alt="Rectangle" caption="<em>Asset Extended Attributes</em>" class="border-0" >}}

To add an attachment, such as an image of your asset, select `Add Attachment` and then select the plus symbol.

{{< img src="AssetAttachmentQS.png" alt="Rectangle" caption="<em>Asset Attachment</em>" class="border-0" >}}

5. Once complete, click `Create Asset`.

{{< img src="AssetCreateQS.png" alt="Rectangle" caption="<em>Create the Asset</em>" class="border-0" >}}

6. `Manage Assets` (default view) is where you may view a list of your Assets within the UI.

{{< img src="AssetManageQS.png" alt="Rectangle" caption="<em>Managing Assets</em>" class="border-0" >}}

7. To view a detailed history of your Asset, click on the small eye symbol ( ![](EyeSymbol.png) ) to the right of the Asset in the Manage view.

{{< img src="AssetViewQS.png" alt="Rectangle" caption="<em>Viewing an Asset</em>" class="border-0" >}}

Here you will see the details entered earlier; The Extended Attributes and the history of any Events recorded on the Asset.

The first Event in an Asset's Lifecycle will always be the 'Asset Creation' Event, in the next section you will find out how to create your own events against an Asset.

## Creating Events

1. When viewing your Asset, click the `Record Event` button.

{{< img src="EventRecordQS.png" alt="Rectangle" caption="<em>Recording an Event</em>" class="border-0" >}}

2. You will see the following form, where you can enter an Event `Type` and `Description`.

{{< img src="EventInformationQS.png" alt="Rectangle" caption="<em>Entering Event Details</em>" class="border-0" >}}

3. Using the Tabs enables you to then enter both Event and Asset attributes.

* `Event Attributes` - Attributes specific to an Event i.e. signifying _when_ a new frame was ordered
* `Asset Attributes` - Attributes of the Asset that may change as a result of the Event i.e. the color of the new frame

Select the `Add Attribute` button on each field to add your own custom Key-Value pairs.

For example:

{{< img src="EventAttributesQS.png" alt="Rectangle" caption="<em>Event Specific Attributes</em>" class="border-0" >}}

{{< img src="EventAssetAttributesQS.png" alt="Rectangle" caption="<em>Event Asset Attributes</em>" class="border-0" >}}

Here you see that someone noted a new frame has been ordered in the Event, and has also recorded the color of the frame using a newly defined `Frame Color` Asset Attribute.

Note that every Event will always have a `timestamp_accepted` and `principal_accepted` Event Attributes once created, which records _when_ _who_ performed what, as submitted to RKVST; this is added automatically at Event Creation.

Similarly, PDFs or images can also be attached to an Event in the same way as an Asset. 

Attaching files is beneficial when storing contextual and associated material for posterity. For example, each `Frame Order` Event may have a copy of the invoice for the new frame and a datasheet attached ready for historical inspection and compliance checking.

4. Once you have entered your data, click the `Record Event` Button, to add the Event to your Asset.

You will see that the Asset Attribute that changed is recorded in the Asset View.

{{< img src="EventRecordedQS.png" alt="Rectangle" caption="<em>Submitting the Event</em>" class="border-0" >}}

5. You can use the eye symbol ( ![](EyeSymbol.png) ) to inspect the Event:

{{< img src="EventViewQS.png" alt="Rectangle" caption="<em>Viewing an Event</em>" class="border-0" >}}

Here are the details entered earlier and also a tab that will show both the Event Attributes and Asset Attributes:

{{< img src="EventAttributeViewNT.png" alt="Rectangle" caption="<em>Viewing Event Attributes</em>" class="border-0" >}}

## Adding External Organizations to Allow Sharing

A key aspect of RKVST is the ability to share specific information with multiple external parties, in order to achieve this, you must first import the ID of the External Organization.

### Finding Your Own ID

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Select the Subjects Tab, where your own Organization's ID will be located in the `Self` box.

{{< caution >}} **Caution:** Please do not use the subject info obtained from the copy menu on the login button. {{< /caution >}}

This string is the one you should share with a 3rd Party who wants to share their data with you.

{{< img src="PolicyOBACSubjectSelf.png" alt="Rectangle" caption="<em>Managing Policies</em>" class="border-0" >}}

### Importing External Organization's ID

Once you have an Asset defined, it can be shared both within your department or even to another organization, enhancing the multi-party sharing experience.

{{< note >}}
**Note:** You must request that any external organization you wish to share with find their own Organization's ID using the steps above and share it with you before you can begin sharing Asset data with them.
{{< /note >}}

1. As a Root User, navigate to `Access Policies`.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Select the Subjects Tab and then `Import Subject`.

{{< img src="PolicyOBACSubjectImport.png" alt="Rectangle" caption="<em>Importing a Subject</em>" class="border-0" >}}

3. You will be presented with a new form: `Subject String` is the ID of the Organization that you wish to share Asset evidence with, `Name` is a Friendly Name for you to label the imported organization.

{{< img src="PolicyOBACSubjectAdd.png" alt="Rectangle" caption="<em>Adding the Subject</em>" class="border-0" >}}

## Creating an OBAC Sharing Policy

1. Navigate to the `Access Policies` section in the Sidebar.

{{< img src="PolicyManageNT.png" alt="Rectangle" caption="<em>Access Policies</em>" class="border-0" >}}

2. Here you can manage your existing policies, but for now select `Add Policy`.

{{< img src="PolicyAdd.png" alt="Rectangle" caption="<em>Adding a Policy</em>" class="border-0" >}}

3. When you add a policy the following form will appear:

{{< img src="PolicyForm.png" alt="Rectangle" caption="<em>Policy Web Form</em>" class="border-0" >}}

4. You should begin applying filters to your Policy so it applies to the correct assets. Following the example let's filter for `Bike` type Assets in the `Jitsuin Paris` Location.

{{< note >}} **Note:** The applied filters should be an exact match to what has been recorded.  Following the above example, there should be an Asset Type `Bike` and a location of `Jitsuin Paris` within RKVST. {{< /note >}}

{{< img src="PolicyOBACFilterNT.png" alt="Rectangle" caption="<em>Filtering for specific Assets and Locations</em>" class="border-0" >}}

5. Select the `Permissions` Tab and define which Organizations can read and write which Attributes and Events.

{{< img src="PolicyOBACForm.png" alt="Rectangle" caption="<em>Default view of Policy Permissions</em>" class="border-0" >}}

6. In the example let's use the `Organization` actor, implying OBAC (Organization Based Access Control). 

Enter the Friendly Name of the Organization you wish to share with and a pre-populated, drop-down search of the Organizations you have already imported should appear.

{{< note >}} **Note:** You will need to have imported another Organization's ID before you can specify a policy to share information with that Organization. {{< /note >}}

{{< img src="PolicyOBACUsers.png" alt="Rectangle" caption="<em>Adding a specific User to a Policy</em>" class="border-0" >}}

7. Once the relevant details are complete, add the Permission Group to the policy by selecting `Add Permission Group`.

Note that the examples includes RKVST-significant attributes: `arc_display_name` and `arc_display_type` which allows visibility to the External Organization of the Name and Type of Asset being shared. 

{{< img src="PolicyPermissionsQS.png" alt="Rectangle" caption="<em>Permitted Attributes on an Asset</em>" class="border-0" >}}

8. Once complete, select `Create Policy` and check the Asset is shared appropriately.

{{< img src="PolicyOBACPermissionsQS.png" alt="Rectangle" caption="<em>Submitting a Policy</em>" class="border-0" >}}

Mandy should be able to see only the `Name` and `Type` of Asset and the Asset's custom `Frame Color` attribute.

{{< img src="PolicyOBACMandyViewNT.png" alt="Rectangle" caption="<em>Mandy's view as a Root User of the External Organization</em>" class="border-0" >}}

By comparison our own Tenancy's Root User, Jill, can see the full details of the Asset:

{{< img src="PolicyOBACJillViewNT.png" alt="Rectangle" caption="<em>Jill's view as a Root User</em>" class="border-0" >}}

9. If Mandy wishes to then share what she can with Non-Root Users in her organization, it is her responsibility to create an ABAC Policy as she would any other Asset.

ABAC and OBAC Policy Creation has many fine-grained controls, head over to the [IAM Policies API Reference](../../api-reference/iam-policies-api/) to find out more.
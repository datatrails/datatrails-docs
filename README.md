[![Board Status](https://dev.azure.com/jitsuin/0629f48c-3979-4bbc-9026-cb06b3dfd0ae/291fa371-1bc4-4424-b88a-96b6f89c9a66/_apis/work/boardbadge/423c32a8-aeab-4b37-91eb-d1a4d04348b3)](https://dev.azure.com/jitsuin/0629f48c-3979-4bbc-9026-cb06b3dfd0ae/_boards/board/t/291fa371-1bc4-4424-b88a-96b6f89c9a66/Microsoft.RequirementCategory)
# RKVST Documentation

This is the Home of the RKVST Documentation.

RKVST provides Continuous Assurance as a Service to attest trustworthiness of Assets and boost confidence in critical decisions.  Find out more on our [website](https://rkvst.com).

## Contributing

To contribute to these Docs, please refer to our [Contributing Guidelines](https://docs.rkvst.com/contributing/getting-started/pulling-and-building-rkvst-docs/).

We'll happily review any suggestions!

## Getting Started

1. To begin, pull the latest RKVST docs from Github.

```bash
git clone git@github.com:rkvst/rkvst-docs.git
```

2. Move into the directory.

```bash
cd rkvst-doks
```

3. Install the DOKS Dependencies.

```bash
npm install
```

4. To run a local RKVST Docs Server, it is advisable to use the `rkvst-doks` wrapper.

```bash
rkvst-doks start
```

This will build a local version of the server that can be accessed at [http://localhost:1313](https://localhost:1313).


## Credits

This Documentation was put together using some amazing opensource tools and projects; this is a list of known projects included but is not exhaustive.

* The wonderful [Doks Theme](https://github.com/h-enk/doks). License: [MIT](https://github.com/h-enk/doks/blob/master/LICENSE)
* Built on top of [Hugo](https://github.com/gohugoio/hugo). License: [Apache License 2.0](https://github.com/gohugoio/hugo/blob/master/LICENSE)
* With inspiration and examples from the [Kubernetes Docs](https://github.com/kubernetes/website). License: [CC BY-SA 4.0](https://github.com/kubernetes/website/blob/master/LICENSE)
* Screenshotting dynamically handled by the [Robot Framework](https://github.com/robotframework/robotframework) using the [Selenium2](https://github.com/SeleniumHQ/selenium) package. Licenses: [Apache License 2.0](https://github.com/robotframework/robotframework/blob/master/LICENSE.txt) and [Apache License 2.0](https://github.com/SeleniumHQ/selenium/blob/trunk/LICENSE) respectively
* Hosted by GitHub Pages and built using GH Actions

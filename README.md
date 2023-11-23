# DataTrails Documentation

This is the Home of the DataTrails Documentation.

DataTrails provides Provenance as a Service to attest trustworthiness of Assets and boost confidence in digital decisions.  Find out more on our [website](https://DataTrails.ai).

## Contributing

To contribute to these Docs, please refer to our [Contributing Guidelines](./content/contributing/getting-started/pulling-and-building-datatrails-docs/index.md).

We'll happily review any suggestions!

## Getting Started

1. To begin, pull the latest DataTrails docs from Github.

```bash
git clone git@github.com/datatrails/datatrails-docs.git
```

2. Move into the directory.

```bash
cd datatrails-docs
```

3. Install the DOKS Dependencies.

```bash
npm install
```

4. To run a local DataTrails Docs Server, it is advisable to use the `rkvst-doks` wrapper.

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

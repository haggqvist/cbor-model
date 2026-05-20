# Changelog

## [0.7.2](https://github.com/haggqvist/cbor-model/compare/v0.7.1...v0.7.2) (2026-05-20)


### Bug Fixes

* remove type hint from model_serializer ([ed498c0](https://github.com/haggqvist/cbor-model/commit/ed498c0e916b59627a665c2c4c7a49628fb6ae67))
* unknown_keys docstring default value ([649de1c](https://github.com/haggqvist/cbor-model/commit/649de1ce8129981e54134d36b92bd346a58ce18a))

## [0.7.1](https://github.com/haggqvist/cbor-model/compare/v0.7.0...v0.7.1) (2026-05-19)


### Bug Fixes

* change default for unknown_keys ([371e91b](https://github.com/haggqvist/cbor-model/commit/371e91b13294bde054dbce0d745cb28a8dfb5222))

## [0.7.0](https://github.com/haggqvist/cbor-model/compare/v0.6.0...v0.7.0) (2026-05-19)


### Features

* unknown_keys handling in CBORConfig ([3a9bffd](https://github.com/haggqvist/cbor-model/commit/3a9bffd5c3ab618eb1a7df1fae3592967144138c))


### Bug Fixes

* add explicit CBOR mapping type guards ([3f9492d](https://github.com/haggqvist/cbor-model/commit/3f9492d5d174f8b90f549ab8945248bcfbc64153))
* improve bstr_wrap error handling ([a5f6306](https://github.com/haggqvist/cbor-model/commit/a5f630624d12199199a86471c9308b5f96c75d64))
* surface context when exclude_if callback raises ([014a9f7](https://github.com/haggqvist/cbor-model/commit/014a9f761e1913eb299ce9fb89000384b0436e2b))
* upgrade to cbor2&gt;=6.1 ([d473bc1](https://github.com/haggqvist/cbor-model/commit/d473bc158c8144edcd8e06fff267282f8e67b0a5))

## [0.6.0](https://github.com/haggqvist/cbor-model/compare/v0.5.0...v0.6.0) (2026-05-05)


### Features

* export EnumStyle and TypeConverter ([9fcd7ce](https://github.com/haggqvist/cbor-model/commit/9fcd7ceb170d566aa64ef7228d665faea83a0770))


### Bug Fixes

* propagate nested constraints in TypeConverter.convert ([8a37a14](https://github.com/haggqvist/cbor-model/commit/8a37a14b5def9774263624864d00f76da334e116))

## [0.5.0](https://github.com/haggqvist/cbor-model/compare/v0.4.1...v0.5.0) (2026-04-27)


### Features

* range constraints for maps ([a6350b3](https://github.com/haggqvist/cbor-model/commit/a6350b3201ff908a0812d328e8ed94391b5130f3))


### Bug Fixes

* infer cddl map constraints from type ([85556b4](https://github.com/haggqvist/cbor-model/commit/85556b4f00665a240661526721c272689c05e92f))
* raise error on invalid RangeConstraint ([bc09f59](https://github.com/haggqvist/cbor-model/commit/bc09f59a60bf32d839d5e35eda795524ee668f08))

## [0.4.1](https://github.com/haggqvist/cbor-model/compare/v0.4.0...v0.4.1) (2026-04-23)


### Bug Fixes

* emit PEP 695 type aliases as top-level CDDL rules ([#7](https://github.com/haggqvist/cbor-model/issues/7)) ([3c681b2](https://github.com/haggqvist/cbor-model/commit/3c681b2f28358e1c3a66d2b475019683b1b35329))
* include CBOR tag on models in CDDL ([#8](https://github.com/haggqvist/cbor-model/issues/8)) ([c9bb5b5](https://github.com/haggqvist/cbor-model/commit/c9bb5b5143b0470d112fc91361db79c7c1560f2b))

## [0.4.0](https://github.com/haggqvist/cbor-model/compare/v0.3.0...v0.4.0) (2026-04-22)


### Features

* add aliases for common int types ([cc1903c](https://github.com/haggqvist/cbor-model/commit/cc1903cccc44dd5cf9cdc1ea9a23b60aa964668d))
* produce CDDL for enums as choice ([49137ad](https://github.com/haggqvist/cbor-model/commit/49137ad2c31426bedc36d4e763f1e5e606adef99))


### Bug Fixes

* emit precise RFC 8610 integer bounds ([33c9a03](https://github.com/haggqvist/cbor-model/commit/33c9a0346e64a31dcc467e87645f9e8118f967df))
* enforce RFC 8610 .size bounds for strings and bytes ([c5defb9](https://github.com/haggqvist/cbor-model/commit/c5defb9b742bb63f35fe6052f0d78b062359e8b5))

## [0.3.0](https://github.com/haggqvist/cbor-model/compare/v0.2.0...v0.3.0) (2026-04-22)


### Features

* emit snake_case named keys and add CBORField.description ([7a22520](https://github.com/haggqvist/cbor-model/commit/7a225207613e13c8b8202c38126ec22a2b7c5985))


### Bug Fixes

* remove extra trailing comma for description ([e18d0d6](https://github.com/haggqvist/cbor-model/commit/e18d0d69f624c7e2a8779559488404b87ce18001))

## [0.2.0](https://github.com/haggqvist/cbor-model/compare/v0.1.0...v0.2.0) (2026-04-15)


### Features

* add bstr wrapping to CBORField ([7df112f](https://github.com/haggqvist/cbor-model/commit/7df112f92914f656e0be155f22453b6023657ca5))


### Bug Fixes

* produce correct CDDL for Literal ([3af38d7](https://github.com/haggqvist/cbor-model/commit/3af38d7c13d929476a844a56665ebc19ff5b6892))
* support X|Y union syntax on python &lt; 3.14 ([cb6163c](https://github.com/haggqvist/cbor-model/commit/cb6163c4edfab354a0e43bf15a383ab6050d2b01))

## 0.1.0 (2026-03-11)


### Features

* initial implementation ([2d040b4](https://github.com/haggqvist/cbor-model/commit/2d040b4247feb06233db17d300ddbd64820660b5))

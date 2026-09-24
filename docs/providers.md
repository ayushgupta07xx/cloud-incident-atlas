# Providers

24 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 11002 | 4.5h | 18.1h | 1057.6h |
| Cloudflare | cdn | 6714 | 4.0h | 8.2h | 5350.4h |
| Grafana Cloud | observability | 760 | 1.5h | 19.0h | 2571.2h |
| GitHub | devtools | 625 | 1.1h | 4.9h | 62.0h |
| DigitalOcean | cloud | 506 | 2.4h | 9.6h | 304.2h |
| Supabase | paas | 409 | 2.5h | 18.1h | 2129.0h |
| Vercel | paas | 389 | 1.2h | 6.0h | 339.2h |
| Sentry | observability | 341 | 1.4h | 6.1h | 668.4h |
| CircleCI | devtools | 312 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 273 | 2.0h | 23.8h | 4467.0h |
| Confluent Cloud | data | 259 | 3.2h | 27.4h | 2821.4h |
| Elastic Cloud | observability | 258 | 3.2h | 24.1h | 364.1h |
| Discord | comms | 223 | 56m | 4.9h | 664.8h |
| Netlify | paas | 220 | 40m | 3.3h | 347.3h |
| Snowflake | data | 200 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 168 | 2.0h | 32.8h | 1944.0h |
| Datadog | observability | 124 | 1.2h | 3.8h | 49.9h |
| New Relic | observability | 106 | 1.1h | 5.2h | 52.3h |
| OpenAI | ai | 79 | 1.7h | 10.1h | 42.4h |
| Amazon Web Services | cloud | 73 | — | — | — |
| npm | devtools | 63 | 1.7h | 5.4h | 20.9h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| HashiCorp Cloud | devtools | 37 | 3.3h | 24.9h | 120.0h |
| Google Cloud Platform | cloud | 6 | 7.4h | — | 516.0h |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 79 | 10 |
| cdn | 1 | 6714 | 131 |
| cloud | 3 | 585 | 34 |
| comms | 3 | 11393 | 120 |
| data | 3 | 732 | 267 |
| devtools | 5 | 1076 | 219 |
| observability | 5 | 1589 | 566 |
| paas | 3 | 1018 | 234 |

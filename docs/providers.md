# Providers

25 providers with recorded incidents. Percentiles are suppressed below n=10 and medians below n=5, so thin samples show an em dash rather than a number the data cannot support. Azure is tracked but absent here: it publishes only active incidents, so it contributes no historical records.

| Provider | Category | Incidents | Median MTTR | p90 MTTR | Longest |
| --- | --- | ---: | ---: | ---: | ---: |
| Twilio | comms | 11102 | 4.5h | 18.2h | 1057.6h |
| Cloudflare | cdn | 6759 | 4.0h | 8.4h | 5350.4h |
| Grafana Cloud | observability | 774 | 1.5h | 18.9h | 2571.2h |
| GitHub | devtools | 636 | 1.1h | 4.9h | 62.0h |
| DigitalOcean | cloud | 509 | 2.4h | 9.5h | 304.2h |
| Supabase | paas | 441 | 2.5h | 20.6h | 2129.0h |
| Vercel | paas | 394 | 1.2h | 6.1h | 339.2h |
| Sentry | observability | 342 | 1.4h | 6.0h | 668.4h |
| CircleCI | devtools | 319 | 1.1h | 8.0h | 96.0h |
| MongoDB Atlas | data | 278 | 2.0h | 23.4h | 4467.0h |
| Confluent Cloud | data | 264 | 3.2h | 27.0h | 2821.4h |
| Elastic Cloud | observability | 260 | 3.2h | 25.7h | 708.5h |
| Netlify | paas | 225 | 38m | 3.1h | 347.3h |
| Discord | comms | 224 | 56m | 4.9h | 664.8h |
| Snowflake | data | 204 | 2.0h | 9.9h | 1801.6h |
| Zoom | comms | 186 | 2.0h | 29.6h | 1944.0h |
| Datadog | observability | 127 | 1.2h | 3.8h | 49.9h |
| New Relic | observability | 108 | 1.1h | 5.2h | 52.3h |
| OpenAI | ai | 108 | 1.8h | 10.2h | 70.7h |
| Amazon Web Services | cloud | 79 | — | — | — |
| npm | devtools | 64 | 1.8h | 5.8h | 20.9h |
| HashiCorp Cloud | devtools | 40 | 3.0h | 27.5h | 126.1h |
| Atlassian | devtools | 39 | 2.0h | 37.4h | 261.0h |
| Google Cloud Platform | cloud | 7 | 10.7h | — | 516.0h |
| Microsoft Azure | cloud | 1 | — | — | — |

## By category

| Category | Providers | Incidents | Major or worse |
| --- | ---: | ---: | ---: |
| ai | 1 | 108 | 15 |
| cdn | 1 | 6759 | 133 |
| cloud | 4 | 596 | 35 |
| comms | 3 | 11512 | 120 |
| data | 3 | 746 | 276 |
| devtools | 5 | 1098 | 229 |
| observability | 5 | 1611 | 572 |
| paas | 3 | 1060 | 245 |

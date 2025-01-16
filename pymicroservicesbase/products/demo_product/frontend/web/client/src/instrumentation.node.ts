import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'
import { Resource } from '@opentelemetry/resources'
import { NodeSDK } from '@opentelemetry/sdk-node'
import { ConsoleSpanExporter, SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node'
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions'
const { PeriodicExportingMetricReader, ConsoleMetricExporter } = await import(
  '@opentelemetry/sdk-metrics'
);


const sdk = new NodeSDK({
  traceExporter: new ConsoleSpanExporter(),
  instrumentations: [

  ],
  resource: new Resource({
    [ATTR_SERVICE_NAME]: 'ycapp',
  }),
  spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
  autoDetectResources:true,
  metricReader: new PeriodicExportingMetricReader({
    exporter: new ConsoleMetricExporter(),
  }),
})

process.on('SIGTERM', () =>
    sdk
        .shutdown()
        .then(
            () => console.log('Opentelementry SDK shut down successfully'),
            (err:any) => console.log('Error shutting down opentelementry SDK', err)
        )
        .finally(() => process.exit(0))
);

sdk.start();

// /** @type {import('next').NextConfig} */
// @ts-nocheck

import { PHASE_DEVELOPMENT_SERVER } from 'next/constants';
import type { NextConfig } from 'next'


const isDebuggerEnabled = process.env.DEBUGGER === 'true';
const debuggerPort = process.env.DEBUGGER_PORT || '9229';
const debuggerHost = process.env.DEBUGGER_HOST || 'localhost';

const config = async (phase: string, { defaultConfig }: { defaultConfig: NextConfig}) => {
    /**
   * @type {import('next').NextConfig}
   */
    const nextConfig:NextConfig = {
      // output: 'export', // change to build that u can serve on backend , its better to not use this in big apps , where need to decouple backend and frontend.
      // distDir: 'dist',
      // reactStrictMode: true,
      // swcMinify: true,
      // webpack: (config, context) => {
      //     // Enable polling based on env variable being set
      //     if(true) {
      //       config.watchOptions = {
      //         poll: 500,
      //         aggregateTimeout: 300
      //       }
      //     }
      //     return config
      //   },
      serverExternalPackages: [
        "@opentelemetry/sdk-node",
        "@opentelemetry/instrumentation",
      ],

      pageExtensions: ['ts', 'tsx'],

      webpack(config, context) {


          // camel-case style names from css modules
          config.module.rules
            .find(({oneOf}) => !!oneOf).oneOf
            .filter(({use}) => JSON.stringify(use)?.includes('css-loader'))
            .reduce((acc, {use}) => acc.concat(use), [])
            .forEach(({options}) => {
              if (options.modules) {
                options.modules.exportLocalsConvention = 'camelCase';
              }
            });


          if (isDebuggerEnabled && context.dev) {
            // Modify Node.js process to start with debugging enabled
            // You can add more logic here if you want to handle other aspects of the debugger.
            config.node = {
              ...config.node,
              debug: true, // Enable debugging for Node.js
            };

            // Optionally, you can also configure how the dev server behaves if necessary
            config.devServer = {
              ...config.devServer,
              before(app) {
                // If the debugger is enabled, make sure it starts the server with debugging
                app.listen(debuggerPort, debuggerHost, () => {
                  console.log(`Debugger connected at ${debuggerHost}:${debuggerPort}`);
                });
              },
            };
          }
      // Reduce the number of chunks so we ship a smaller first bundle.
      // This should help reducing TBT
          if (!context.isServer && !context.dev && config.optimization?.splitChunks) {
            config.optimization.splitChunks.maxInitialRequests = 1
          }


          return config;
        },
        eslint:{

        },
        compiler: {
          removeConsole: process.env.NODE_ENV === 'production',
        },
    };

    if (phase === PHASE_DEVELOPMENT_SERVER) {
      return nextConfig;
    }
    return nextConfig;
}

// const nextConfig:NextConfig = {
//     // output: 'export', // change to build that u can serve on backend , its better to not use this in big apps , where need to decouple backend and frontend.
//     // distDir: 'dist',
//     // reactStrictMode: true,
//     // swcMinify: true,
//     // webpack: (config, context) => {
//     //     // Enable polling based on env variable being set
//     //     if(true) {
//     //       config.watchOptions = {
//     //         poll: 500,
//     //         aggregateTimeout: 300
//     //       }
//     //     }
//     //     return config
//     //   },

//     pageExtensions: ['ts', 'tsx'],

//     webpack(config, context) {


//         // camel-case style names from css modules
//         config.module.rules
//           .find(({oneOf}) => !!oneOf).oneOf
//           .filter(({use}) => JSON.stringify(use)?.includes('css-loader'))
//           .reduce((acc, {use}) => acc.concat(use), [])
//           .forEach(({options}) => {
//             if (options.modules) {
//               options.modules.exportLocalsConvention = 'camelCase';
//             }
//           });


//         if (isDebuggerEnabled && context.dev) {
//           // Modify Node.js process to start with debugging enabled
//           // You can add more logic here if you want to handle other aspects of the debugger.
//           config.node = {
//             ...config.node,
//             debug: true, // Enable debugging for Node.js
//           };

//           // Optionally, you can also configure how the dev server behaves if necessary
//           config.devServer = {
//             ...config.devServer,
//             before(app) {
//               // If the debugger is enabled, make sure it starts the server with debugging
//               app.listen(debuggerPort, debuggerHost, () => {
//                 console.log(`Debugger connected at ${debuggerHost}:${debuggerPort}`);
//               });
//             },
//           };
//         }
//     // Reduce the number of chunks so we ship a smaller first bundle.
//     // This should help reducing TBT
//         if (!context.isServer && !context.dev && config.optimization?.splitChunks) {
//           config.optimization.splitChunks.maxInitialRequests = 1
//         }


//         return config;
//       },
//       eslint:{

//       },
//       compiler: {
//         removeConsole: process.env.NODE_ENV === 'production',
//       },
// };

export default config;

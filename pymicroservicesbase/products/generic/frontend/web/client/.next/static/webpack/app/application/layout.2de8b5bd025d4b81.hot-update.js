"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
self["webpackHotUpdate_N_E"]("app/application/layout",{

/***/ "(app-pages-browser)/./src/components/common/logo/LogoWithName.tsx":
/*!*****************************************************!*\
  !*** ./src/components/common/logo/LogoWithName.tsx ***!
  \*****************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var next_image__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! next/image */ \"(app-pages-browser)/./node_modules/next/dist/api/image.js\");\n\n\n// const LogoWithName: React.FC<LogoWithNameProps> = ({ width = 40, height = 40 }) => {\n//   return (\n//     <div className=\"flex items-center\">\n//       <Image src={layoutConfig.brand.logo} alt={layoutConfig.brand.name} width={width} height={height}  style={{\n//       }} />\n//       <span className=\"ml-2 text-lg font-bold\">{layoutConfig.brand.name}</span>\n//     </div>\n//   );\n// };\nconst LogoWithName = (param)=>{\n    let { width = 40, height = 40, title = \"Logo\" } = param;\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n        className: \"flex items-center\",\n        children: [\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(next_image__WEBPACK_IMPORTED_MODULE_1__[\"default\"], {\n                src: \"/assets/logo.png\",\n                alt: \"logo\",\n                width: width,\n                height: height,\n                style: {\n                    userSelect: \"none\",\n                    pointerEvents: \"none\"\n                }\n            }, void 0, false, {\n                fileName: \"/code/src/components/common/logo/LogoWithName.tsx\",\n                lineNumber: 26,\n                columnNumber: 7\n            }, undefined),\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"span\", {\n                className: \"ml-2 text-lg font-bold\",\n                children: logo\n            }, void 0, false, {\n                fileName: \"/code/src/components/common/logo/LogoWithName.tsx\",\n                lineNumber: 30,\n                columnNumber: 7\n            }, undefined)\n        ]\n    }, void 0, true, {\n        fileName: \"/code/src/components/common/logo/LogoWithName.tsx\",\n        lineNumber: 25,\n        columnNumber: 5\n    }, undefined);\n};\n_c = LogoWithName;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LogoWithName);\nvar _c;\n$RefreshReg$(_c, \"LogoWithName\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9jb21wb25lbnRzL2NvbW1vbi9sb2dvL0xvZ29XaXRoTmFtZS50c3giLCJtYXBwaW5ncyI6Ijs7Ozs7OztBQUMrQjtBQVkvQix1RkFBdUY7QUFDdkYsYUFBYTtBQUNiLDBDQUEwQztBQUMxQyxtSEFBbUg7QUFDbkgsY0FBYztBQUNkLGtGQUFrRjtBQUNsRixhQUFhO0FBQ2IsT0FBTztBQUNQLEtBQUs7QUFDTCxNQUFNQyxlQUE0QztRQUFDLEVBQUVDLFFBQVEsRUFBRSxFQUFFQyxTQUFTLEVBQUUsRUFBRUMsUUFBTyxNQUFNLEVBQUU7SUFDM0YscUJBQ0UsOERBQUNDO1FBQUlDLFdBQVU7OzBCQUNiLDhEQUFDTixrREFBS0E7Z0JBQUNPLEtBQUs7Z0JBQW9CQyxLQUFLO2dCQUFRTixPQUFPQTtnQkFBT0MsUUFBUUE7Z0JBQVNNLE9BQU87b0JBQ2pGQyxZQUFXO29CQUNYQyxlQUFjO2dCQUNoQjs7Ozs7OzBCQUNBLDhEQUFDQztnQkFBS04sV0FBVTswQkFBMEJPOzs7Ozs7Ozs7Ozs7QUFHaEQ7S0FWTVo7QUFhTixpRUFBZUEsWUFBWUEsRUFBQyIsInNvdXJjZXMiOlsiL2NvZGUvc3JjL2NvbXBvbmVudHMvY29tbW9uL2xvZ28vTG9nb1dpdGhOYW1lLnRzeCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBsYXlvdXRDb25maWcgfSBmcm9tICdAL2NvbmZpZyc7XG5pbXBvcnQgSW1hZ2UgZnJvbSAnbmV4dC9pbWFnZSc7XG5cblxuaW50ZXJmYWNlIExvZ29XaXRoTmFtZVByb3BzIHtcbi8vICAgc3JjOiBzdHJpbmc7XG4vLyAgIGFsdDogc3RyaW5nO1xuLy8gICBuYW1lOiBzdHJpbmc7XG4gIHdpZHRoPzogbnVtYmVyO1xuICBoZWlnaHQ/OiBudW1iZXI7XG4gIGxvZ28/OiBzdHJpbmc7XG59XG5cbi8vIGNvbnN0IExvZ29XaXRoTmFtZTogUmVhY3QuRkM8TG9nb1dpdGhOYW1lUHJvcHM+ID0gKHsgd2lkdGggPSA0MCwgaGVpZ2h0ID0gNDAgfSkgPT4ge1xuLy8gICByZXR1cm4gKFxuLy8gICAgIDxkaXYgY2xhc3NOYW1lPVwiZmxleCBpdGVtcy1jZW50ZXJcIj5cbi8vICAgICAgIDxJbWFnZSBzcmM9e2xheW91dENvbmZpZy5icmFuZC5sb2dvfSBhbHQ9e2xheW91dENvbmZpZy5icmFuZC5uYW1lfSB3aWR0aD17d2lkdGh9IGhlaWdodD17aGVpZ2h0fSAgc3R5bGU9e3tcbi8vICAgICAgIH19IC8+XG4vLyAgICAgICA8c3BhbiBjbGFzc05hbWU9XCJtbC0yIHRleHQtbGcgZm9udC1ib2xkXCI+e2xheW91dENvbmZpZy5icmFuZC5uYW1lfTwvc3Bhbj5cbi8vICAgICA8L2Rpdj5cbi8vICAgKTtcbi8vIH07XG5jb25zdCBMb2dvV2l0aE5hbWU6IFJlYWN0LkZDPExvZ29XaXRoTmFtZVByb3BzPiA9ICh7IHdpZHRoID0gNDAsIGhlaWdodCA9IDQwLCB0aXRsZSA9XCJMb2dvXCIgfSkgPT4ge1xuICByZXR1cm4gKFxuICAgIDxkaXYgY2xhc3NOYW1lPVwiZmxleCBpdGVtcy1jZW50ZXJcIj5cbiAgICAgIDxJbWFnZSBzcmM9e1wiL2Fzc2V0cy9sb2dvLnBuZ1wifSBhbHQ9e1wibG9nb1wifSB3aWR0aD17d2lkdGh9IGhlaWdodD17aGVpZ2h0fSAgc3R5bGU9e3tcbiAgICAgICAgdXNlclNlbGVjdDpcIm5vbmVcIixcbiAgICAgICAgcG9pbnRlckV2ZW50czpcIm5vbmVcIlxuICAgICAgfX0gLz5cbiAgICAgIDxzcGFuIGNsYXNzTmFtZT1cIm1sLTIgdGV4dC1sZyBmb250LWJvbGRcIj57bG9nb308L3NwYW4+XG4gICAgPC9kaXY+XG4gICk7XG59O1xuXG5cbmV4cG9ydCBkZWZhdWx0IExvZ29XaXRoTmFtZTtcbiJdLCJuYW1lcyI6WyJJbWFnZSIsIkxvZ29XaXRoTmFtZSIsIndpZHRoIiwiaGVpZ2h0IiwidGl0bGUiLCJkaXYiLCJjbGFzc05hbWUiLCJzcmMiLCJhbHQiLCJzdHlsZSIsInVzZXJTZWxlY3QiLCJwb2ludGVyRXZlbnRzIiwic3BhbiIsImxvZ28iXSwiaWdub3JlTGlzdCI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/components/common/logo/LogoWithName.tsx\n"));

/***/ })

});
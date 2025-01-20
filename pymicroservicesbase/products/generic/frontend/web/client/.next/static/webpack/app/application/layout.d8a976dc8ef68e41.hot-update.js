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

/***/ "(app-pages-browser)/./src/layouts/header/components/nav/NavigationMenu.tsx":
/*!**************************************************************!*\
  !*** ./src/layouts/header/components/nav/NavigationMenu.tsx ***!
  \**************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var framer_motion__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! framer-motion */ \"(app-pages-browser)/./node_modules/framer-motion/dist/es/render/components/motion/proxy.mjs\");\n/* __next_internal_client_entry_do_not_use__ default auto */ \n\nconst NavigationMenuLink = (param)=>{\n    let { label, link } = param;\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(framer_motion__WEBPACK_IMPORTED_MODULE_1__.motion.div, {\n        className: \"relative group\",\n        children: [\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(framer_motion__WEBPACK_IMPORTED_MODULE_1__.motion.div, {\n                className: \"absolute inset-0 bg-gray-800 opacity-0 rounded-md\",\n                whileHover: {\n                    opacity: 0.5\n                },\n                transition: {\n                    opacity: {\n                        duration: 0.5\n                    }\n                }\n            }, void 0, false, {\n                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                lineNumber: 27,\n                columnNumber: 7\n            }, undefined),\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(framer_motion__WEBPACK_IMPORTED_MODULE_1__.motion.a, {\n                href: link || \"/\",\n                className: \"text-white text-lg font-semibold hover:text-blue-500 transition-all relative z-10\",\n                children: label\n            }, void 0, false, {\n                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                lineNumber: 33,\n                columnNumber: 7\n            }, undefined)\n        ]\n    }, void 0, true, {\n        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n        lineNumber: 25,\n        columnNumber: 5\n    }, undefined);\n};\n_c = NavigationMenuLink;\nconst NavigationMenu = (param)=>{\n    let { rows } = param;\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"nav\", {\n        className: \"w-full flex justify-center\",\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n            className: \"flex flex-wrap justify-center gap-8\",\n            children: rows.map((row, rowIndex)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                    className: \"flex space-x-8\",\n                    children: row.columns.map((col, colIndex)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                            className: \"relative group\",\n                            children: [\n                                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(NavigationMenuLink, {\n                                    label: col.label,\n                                    link: col.link\n                                }, void 0, false, {\n                                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                    lineNumber: 54,\n                                    columnNumber: 17\n                                }, undefined),\n                                col.rows && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                                    className: \"absolute top-full left-0 bg-gray-800 opacity-0 group-hover:opacity-100 transition-all duration-300 rounded-md\",\n                                    children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                                        className: \"p-4\",\n                                        children: col.rows.map((row, rowIndex)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                                                className: \"space-y-2\",\n                                                children: row.columns.map((subCol, colIndex)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                                                        className: \"py-2\",\n                                                        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(NavigationMenuLink, {\n                                                            label: subCol.label,\n                                                            link: subCol.link\n                                                        }, void 0, false, {\n                                                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                                            lineNumber: 63,\n                                                            columnNumber: 31\n                                                        }, undefined)\n                                                    }, colIndex, false, {\n                                                        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                                        lineNumber: 62,\n                                                        columnNumber: 29\n                                                    }, undefined))\n                                            }, rowIndex, false, {\n                                                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                                lineNumber: 60,\n                                                columnNumber: 25\n                                            }, undefined))\n                                    }, void 0, false, {\n                                        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                        lineNumber: 58,\n                                        columnNumber: 21\n                                    }, undefined)\n                                }, void 0, false, {\n                                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                    lineNumber: 57,\n                                    columnNumber: 19\n                                }, undefined)\n                            ]\n                        }, colIndex, true, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 52,\n                            columnNumber: 15\n                        }, undefined))\n                }, rowIndex, false, {\n                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                    lineNumber: 49,\n                    columnNumber: 11\n                }, undefined))\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n            lineNumber: 47,\n            columnNumber: 7\n        }, undefined)\n    }, void 0, false, {\n        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n        lineNumber: 45,\n        columnNumber: 5\n    }, undefined);\n};\n_c1 = NavigationMenu;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (NavigationMenu);\nvar _c, _c1;\n$RefreshReg$(_c, \"NavigationMenuLink\");\n$RefreshReg$(_c1, \"NavigationMenu\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9sYXlvdXRzL2hlYWRlci9jb21wb25lbnRzL25hdi9OYXZpZ2F0aW9uTWVudS50c3giLCJtYXBwaW5ncyI6Ijs7Ozs7OztBQUN1QztBQXFCdkMsTUFBTUMscUJBQW1EO1FBQUMsRUFBRUMsS0FBSyxFQUFFQyxJQUFJLEVBQUU7SUFDdkUscUJBQ0UsOERBQUNILGlEQUFNQSxDQUFDSSxHQUFHO1FBQUNDLFdBQVU7OzBCQUVwQiw4REFBQ0wsaURBQU1BLENBQUNJLEdBQUc7Z0JBQ1RDLFdBQVU7Z0JBQ1ZDLFlBQVk7b0JBQUVDLFNBQVM7Z0JBQUk7Z0JBQzNCQyxZQUFZO29CQUFFRCxTQUFTO3dCQUFFRSxVQUFVO29CQUFJO2dCQUFFOzs7Ozs7MEJBRzNDLDhEQUFDVCxpREFBTUEsQ0FBQ1UsQ0FBQztnQkFDUEMsTUFBTVIsUUFBUTtnQkFDZEUsV0FBVTswQkFFVEg7Ozs7Ozs7Ozs7OztBQUlUO0tBbEJNRDtBQW9CTixNQUFNVyxpQkFBZ0Q7UUFBQyxFQUFFQyxJQUFJLEVBQUU7SUFDN0QscUJBQ0UsOERBQUNDO1FBQUlULFdBQVU7a0JBRWIsNEVBQUNEO1lBQUlDLFdBQVU7c0JBQ1pRLEtBQUtFLEdBQUcsQ0FBQyxDQUFDQyxLQUFLQyx5QkFDZCw4REFBQ2I7b0JBQW1CQyxXQUFVOzhCQUUzQlcsSUFBSUUsT0FBTyxDQUFDSCxHQUFHLENBQUMsQ0FBQ0ksS0FBS0MseUJBQ3JCLDhEQUFDaEI7NEJBQW1CQyxXQUFVOzs4Q0FFNUIsOERBQUNKO29DQUFtQkMsT0FBT2lCLElBQUlqQixLQUFLO29DQUFFQyxNQUFNZ0IsSUFBSWhCLElBQUk7Ozs7OztnQ0FFbkRnQixJQUFJTixJQUFJLGtCQUNQLDhEQUFDVDtvQ0FBSUMsV0FBVTs4Q0FDYiw0RUFBQ0Q7d0NBQUlDLFdBQVU7a0RBQ1pjLElBQUlOLElBQUksQ0FBQ0UsR0FBRyxDQUFDLENBQUNDLEtBQUtDLHlCQUNsQiw4REFBQ2I7Z0RBQW1CQyxXQUFVOzBEQUMzQlcsSUFBSUUsT0FBTyxDQUFDSCxHQUFHLENBQUMsQ0FBQ00sUUFBUUQseUJBQ3hCLDhEQUFDaEI7d0RBQW1CQyxXQUFVO2tFQUM1Qiw0RUFBQ0o7NERBQ0NDLE9BQU9tQixPQUFPbkIsS0FBSzs0REFDbkJDLE1BQU1rQixPQUFPbEIsSUFBSTs7Ozs7O3VEQUhYaUI7Ozs7OytDQUZKSDs7Ozs7Ozs7Ozs7Ozs7OzsyQkFSVkc7Ozs7O21CQUhKSDs7Ozs7Ozs7Ozs7Ozs7O0FBZ0NwQjtNQXRDTUw7QUF3Q04saUVBQWVBLGNBQWNBLEVBQUMiLCJzb3VyY2VzIjpbIi9jb2RlL3NyYy9sYXlvdXRzL2hlYWRlci9jb21wb25lbnRzL25hdi9OYXZpZ2F0aW9uTWVudS50c3giXSwic291cmNlc0NvbnRlbnQiOlsiXCJ1c2UgY2xpZW50XCI7XG5pbXBvcnQgeyBtb3Rpb24gfSBmcm9tICdmcmFtZXItbW90aW9uJztcblxuaW50ZXJmYWNlIE5hdmlnYXRpb25NZW51TGluayB7XG4gIGxhYmVsOiBzdHJpbmc7XG4gIGxpbms/OiBzdHJpbmc7XG59XG5cbmludGVyZmFjZSBDb2x1bW4ge1xuICBsYWJlbDogc3RyaW5nO1xuICBsaW5rPzogc3RyaW5nO1xuICByb3dzPzogQ29sdW1uW107IC8vIE5lc3RlZCByb3dzL2NvbHVtbnMgZm9yIG1vcmUgZmxleGliaWxpdHlcbn1cblxuaW50ZXJmYWNlIFJvdyB7XG4gIGNvbHVtbnM6IENvbHVtbltdOyAvLyBFYWNoIHJvdyBjb250YWlucyBtdWx0aXBsZSBjb2x1bW5zXG59XG5cbmludGVyZmFjZSBOYXZpZ2F0aW9uTWVudVByb3BzIHtcbiAgcm93czogUm93W107IC8vIE1lbnUgY29uZmlndXJhdGlvbiBhcyByb3dzIGFuZCBjb2x1bW5zXG59XG5cbmNvbnN0IE5hdmlnYXRpb25NZW51TGluazogUmVhY3QuRkM8TmF2aWdhdGlvbk1lbnVMaW5rPiA9ICh7IGxhYmVsLCBsaW5rIH0pID0+IHtcbiAgcmV0dXJuIChcbiAgICA8bW90aW9uLmRpdiBjbGFzc05hbWU9XCJyZWxhdGl2ZSBncm91cFwiPlxuICAgICAgey8qIE1vdGlvbiBCYWNrZ3JvdW5kIHdpdGggb3BhY2l0eSBjaGFuZ2Ugb24gaG92ZXIgKi99XG4gICAgICA8bW90aW9uLmRpdlxuICAgICAgICBjbGFzc05hbWU9XCJhYnNvbHV0ZSBpbnNldC0wIGJnLWdyYXktODAwIG9wYWNpdHktMCByb3VuZGVkLW1kXCJcbiAgICAgICAgd2hpbGVIb3Zlcj17eyBvcGFjaXR5OiAwLjUgfX1cbiAgICAgICAgdHJhbnNpdGlvbj17eyBvcGFjaXR5OiB7IGR1cmF0aW9uOiAwLjUgfSB9fVxuICAgICAgLz5cbiAgICAgIHsvKiBMaW5rIFRleHQgKi99XG4gICAgICA8bW90aW9uLmFcbiAgICAgICAgaHJlZj17bGluayB8fCBcIi9cIn1cbiAgICAgICAgY2xhc3NOYW1lPVwidGV4dC13aGl0ZSB0ZXh0LWxnIGZvbnQtc2VtaWJvbGQgaG92ZXI6dGV4dC1ibHVlLTUwMCB0cmFuc2l0aW9uLWFsbCByZWxhdGl2ZSB6LTEwXCJcbiAgICAgID5cbiAgICAgICAge2xhYmVsfVxuICAgICAgPC9tb3Rpb24uYT5cbiAgICA8L21vdGlvbi5kaXY+XG4gICk7XG59O1xuXG5jb25zdCBOYXZpZ2F0aW9uTWVudTogUmVhY3QuRkM8TmF2aWdhdGlvbk1lbnVQcm9wcz4gPSAoeyByb3dzIH0pID0+IHtcbiAgcmV0dXJuIChcbiAgICA8bmF2IGNsYXNzTmFtZT1cInctZnVsbCBmbGV4IGp1c3RpZnktY2VudGVyXCI+XG4gICAgICB7LyogUmVuZGVyIHJvd3MgZHluYW1pY2FsbHkgKi99XG4gICAgICA8ZGl2IGNsYXNzTmFtZT1cImZsZXggZmxleC13cmFwIGp1c3RpZnktY2VudGVyIGdhcC04XCI+XG4gICAgICAgIHtyb3dzLm1hcCgocm93LCByb3dJbmRleCkgPT4gKFxuICAgICAgICAgIDxkaXYga2V5PXtyb3dJbmRleH0gY2xhc3NOYW1lPVwiZmxleCBzcGFjZS14LThcIj5cbiAgICAgICAgICAgIHsvKiBSZW5kZXIgY29sdW1ucyBpbiBlYWNoIHJvdyAqL31cbiAgICAgICAgICAgIHtyb3cuY29sdW1ucy5tYXAoKGNvbCwgY29sSW5kZXgpID0+IChcbiAgICAgICAgICAgICAgPGRpdiBrZXk9e2NvbEluZGV4fSBjbGFzc05hbWU9XCJyZWxhdGl2ZSBncm91cFwiPlxuICAgICAgICAgICAgICAgIHsvKiBSZW5kZXIgTGluayBmb3IgZWFjaCBjb2x1bW4gKi99XG4gICAgICAgICAgICAgICAgPE5hdmlnYXRpb25NZW51TGluayBsYWJlbD17Y29sLmxhYmVsfSBsaW5rPXtjb2wubGlua30gLz5cbiAgICAgICAgICAgICAgICB7LyogUmVuZGVyIHN1Yi1yb3dzIGlmIHRoZXkgZXhpc3QgKi99XG4gICAgICAgICAgICAgICAge2NvbC5yb3dzICYmIChcbiAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiYWJzb2x1dGUgdG9wLWZ1bGwgbGVmdC0wIGJnLWdyYXktODAwIG9wYWNpdHktMCBncm91cC1ob3ZlcjpvcGFjaXR5LTEwMCB0cmFuc2l0aW9uLWFsbCBkdXJhdGlvbi0zMDAgcm91bmRlZC1tZFwiPlxuICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cInAtNFwiPlxuICAgICAgICAgICAgICAgICAgICAgIHtjb2wucm93cy5tYXAoKHJvdywgcm93SW5kZXgpID0+IChcbiAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYga2V5PXtyb3dJbmRleH0gY2xhc3NOYW1lPVwic3BhY2UteS0yXCI+XG4gICAgICAgICAgICAgICAgICAgICAgICAgIHtyb3cuY29sdW1ucy5tYXAoKHN1YkNvbCwgY29sSW5kZXgpID0+IChcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGtleT17Y29sSW5kZXh9IGNsYXNzTmFtZT1cInB5LTJcIj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxOYXZpZ2F0aW9uTWVudUxpbmtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGFiZWw9e3N1YkNvbC5sYWJlbH1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbGluaz17c3ViQ29sLmxpbmt9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgICAgICAgICAgICAgICApKX1cbiAgICAgICAgICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgICAgICAgICAgICkpfVxuICAgICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgICAgICl9XG4gICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgKSl9XG4gICAgICAgICAgPC9kaXY+XG4gICAgICAgICkpfVxuICAgICAgPC9kaXY+XG4gICAgPC9uYXY+XG4gICk7XG59O1xuXG5leHBvcnQgZGVmYXVsdCBOYXZpZ2F0aW9uTWVudTtcbiJdLCJuYW1lcyI6WyJtb3Rpb24iLCJOYXZpZ2F0aW9uTWVudUxpbmsiLCJsYWJlbCIsImxpbmsiLCJkaXYiLCJjbGFzc05hbWUiLCJ3aGlsZUhvdmVyIiwib3BhY2l0eSIsInRyYW5zaXRpb24iLCJkdXJhdGlvbiIsImEiLCJocmVmIiwiTmF2aWdhdGlvbk1lbnUiLCJyb3dzIiwibmF2IiwibWFwIiwicm93Iiwicm93SW5kZXgiLCJjb2x1bW5zIiwiY29sIiwiY29sSW5kZXgiLCJzdWJDb2wiXSwiaWdub3JlTGlzdCI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/layouts/header/components/nav/NavigationMenu.tsx\n"));

/***/ })

});
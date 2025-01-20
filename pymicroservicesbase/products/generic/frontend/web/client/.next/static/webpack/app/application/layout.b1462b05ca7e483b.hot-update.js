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

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/components/motions/Motion */ \"(app-pages-browser)/./src/components/motions/Motion.tsx\");\n/* __next_internal_client_entry_do_not_use__ default auto */ \nvar _s = $RefreshSig$();\n\n\nconst NavigationMenu = (param)=>{\n    let { menuItems } = param;\n    _s();\n    const [activeIndex, setActiveIndex] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(null);\n    const handleMouseEnter = (index)=>{\n        setActiveIndex(index);\n    };\n    const handleMouseLeave = ()=>{\n        setActiveIndex(null);\n    };\n    const renderMenuItems = (items)=>{\n        return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"ul\", {\n            className: \"space-y-2\",\n            children: items.map((item, index)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"li\", {\n                    className: \"hover:bg-gray-700 rounded-md p-2\",\n                    children: [\n                        /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"a\", {\n                            href: item.link,\n                            className: \"block text-white\",\n                            children: item.label\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 39,\n                            columnNumber: 13\n                        }, undefined),\n                        item.subOptions && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                            className: \"pl-4\",\n                            children: [\n                                renderMenuItems(item.subOptions),\n                                \" \"\n                            ]\n                        }, void 0, true, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 44,\n                            columnNumber: 15\n                        }, undefined),\n                        item.description && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"p\", {\n                            className: \"text-sm text-gray-400\",\n                            children: item.description\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 49,\n                            columnNumber: 34\n                        }, undefined),\n                        item.image && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"img\", {\n                            src: item.image,\n                            alt: item.label,\n                            className: \"w-16 h-auto mt-2 rounded-md\"\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 50,\n                            columnNumber: 28\n                        }, undefined)\n                    ]\n                }, index, true, {\n                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                    lineNumber: 38,\n                    columnNumber: 11\n                }, undefined))\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n            lineNumber: 36,\n            columnNumber: 7\n        }, undefined);\n    };\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"nav\", {\n        className: \"w-full flex justify-center\",\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"ul\", {\n            className: \"flex gap-12\",\n            children: menuItems.map((item, index)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"li\", {\n                    className: \"relative group\",\n                    onMouseEnter: ()=>handleMouseEnter(index),\n                    onMouseLeave: handleMouseLeave,\n                    children: [\n                        /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"a\", {\n                            href: item.link,\n                            className: \"text-white text-lg font-semibold hover:text-blue-500 transition-all\",\n                            children: item.label\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 67,\n                            columnNumber: 13\n                        }, undefined),\n                        item.megaMenu && activeIndex === index && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n                            initial: {\n                                opacity: 0,\n                                y: -10\n                            },\n                            animate: {\n                                opacity: 1,\n                                y: 0\n                            },\n                            exit: {\n                                opacity: 0,\n                                y: 10\n                            },\n                            transition: {\n                                duration: 0.3\n                            },\n                            className: \"absolute top-full left-0 w-full bg-gray-900 p-6 grid grid-cols-4 gap-6 z-10\",\n                            children: item.megaMenu\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 75,\n                            columnNumber: 15\n                        }, undefined),\n                        item.subOptions && activeIndex === index && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n                            initial: {\n                                opacity: 0,\n                                y: -10\n                            },\n                            animate: {\n                                opacity: 1,\n                                y: 0\n                            },\n                            exit: {\n                                opacity: 0,\n                                y: 10\n                            },\n                            transition: {\n                                duration: 0.3\n                            },\n                            className: \"absolute top-full left-0 bg-gray-800 text-white shadow-md rounded-md z-10\",\n                            children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"ul\", {\n                                className: \"space-y-2 p-4\",\n                                children: item.subOptions.map((subOption, subIndex)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"li\", {\n                                        className: \"hover:bg-gray-700 rounded-md p-2\",\n                                        children: [\n                                            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"a\", {\n                                                href: subOption.link,\n                                                className: \"block\",\n                                                children: subOption.label\n                                            }, void 0, false, {\n                                                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                                lineNumber: 98,\n                                                columnNumber: 23\n                                            }, undefined),\n                                            subOption.description && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"p\", {\n                                                className: \"text-sm text-gray-400\",\n                                                children: subOption.description\n                                            }, void 0, false, {\n                                                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                                lineNumber: 102,\n                                                columnNumber: 25\n                                            }, undefined),\n                                            subOption.image && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"img\", {\n                                                src: subOption.image,\n                                                alt: subOption.label,\n                                                className: \"w-16 h-auto mt-2 rounded-md\"\n                                            }, void 0, false, {\n                                                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                                lineNumber: 105,\n                                                columnNumber: 25\n                                            }, undefined)\n                                        ]\n                                    }, subIndex, true, {\n                                        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                        lineNumber: 97,\n                                        columnNumber: 21\n                                    }, undefined))\n                            }, void 0, false, {\n                                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                                lineNumber: 95,\n                                columnNumber: 17\n                            }, undefined)\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 88,\n                            columnNumber: 15\n                        }, undefined)\n                    ]\n                }, index, true, {\n                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                    lineNumber: 61,\n                    columnNumber: 11\n                }, undefined))\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n            lineNumber: 59,\n            columnNumber: 7\n        }, undefined)\n    }, void 0, false, {\n        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n        lineNumber: 58,\n        columnNumber: 5\n    }, undefined);\n};\n_s(NavigationMenu, \"E8kOn+IkK/htiBGEqJWkEvOqULU=\");\n_c = NavigationMenu;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (NavigationMenu);\nvar _c;\n$RefreshReg$(_c, \"NavigationMenu\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9sYXlvdXRzL2hlYWRlci9jb21wb25lbnRzL25hdi9OYXZpZ2F0aW9uTWVudS50c3giLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7OztBQUN3QztBQUNTO0FBb0JqRCxNQUFNRyxpQkFBZ0Q7UUFBQyxFQUFFQyxTQUFTLEVBQUU7O0lBQ2xFLE1BQU0sQ0FBQ0MsYUFBYUMsZUFBZSxHQUFHTCwrQ0FBUUEsQ0FBZ0I7SUFFOUQsTUFBTU0sbUJBQW1CLENBQUNDO1FBQ3hCRixlQUFlRTtJQUNqQjtJQUVBLE1BQU1DLG1CQUFtQjtRQUN2QkgsZUFBZTtJQUNqQjtJQUVBLE1BQU1JLGtCQUFrQixDQUFDQztRQUN2QixxQkFDRSw4REFBQ0M7WUFBR0MsV0FBVTtzQkFDWEYsTUFBTUcsR0FBRyxDQUFDLENBQUNDLE1BQU1QLHNCQUNoQiw4REFBQ1E7b0JBQWVILFdBQVU7O3NDQUN4Qiw4REFBQ0k7NEJBQUVDLE1BQU1ILEtBQUtJLElBQUk7NEJBQUVOLFdBQVU7c0NBQzNCRSxLQUFLSyxLQUFLOzs7Ozs7d0JBR1pMLEtBQUtNLFVBQVUsa0JBQ2QsOERBQUNDOzRCQUFJVCxXQUFVOztnQ0FDWkgsZ0JBQWdCSyxLQUFLTSxVQUFVO2dDQUFFOzs7Ozs7O3dCQUlyQ04sS0FBS1EsV0FBVyxrQkFBSSw4REFBQ0M7NEJBQUVYLFdBQVU7c0NBQXlCRSxLQUFLUSxXQUFXOzs7Ozs7d0JBQzFFUixLQUFLVSxLQUFLLGtCQUFJLDhEQUFDQzs0QkFBSUMsS0FBS1osS0FBS1UsS0FBSzs0QkFBRUcsS0FBS2IsS0FBS0ssS0FBSzs0QkFBRVAsV0FBVTs7Ozs7OzttQkFaekRMOzs7Ozs7Ozs7O0lBaUJqQjtJQUVBLHFCQUNFLDhEQUFDcUI7UUFBSWhCLFdBQVU7a0JBQ2IsNEVBQUNEO1lBQUdDLFdBQVU7c0JBQ1hULFVBQVVVLEdBQUcsQ0FBQyxDQUFDQyxNQUFNUCxzQkFDcEIsOERBQUNRO29CQUVDSCxXQUFVO29CQUNWaUIsY0FBYyxJQUFNdkIsaUJBQWlCQztvQkFDckN1QixjQUFjdEI7O3NDQUVkLDhEQUFDUTs0QkFDQ0MsTUFBTUgsS0FBS0ksSUFBSTs0QkFDZk4sV0FBVTtzQ0FFVEUsS0FBS0ssS0FBSzs7Ozs7O3dCQUdaTCxLQUFLaUIsUUFBUSxJQUFJM0IsZ0JBQWdCRyx1QkFDaEMsOERBQUNOLGtFQUFNQTs0QkFDTCtCLFNBQVM7Z0NBQUVDLFNBQVM7Z0NBQUdDLEdBQUcsQ0FBQzs0QkFBRzs0QkFDOUJDLFNBQVM7Z0NBQUVGLFNBQVM7Z0NBQUdDLEdBQUc7NEJBQUU7NEJBQzVCRSxNQUFNO2dDQUFFSCxTQUFTO2dDQUFHQyxHQUFHOzRCQUFHOzRCQUMxQkcsWUFBWTtnQ0FBRUMsVUFBVTs0QkFBSTs0QkFDNUIxQixXQUFVO3NDQUVURSxLQUFLaUIsUUFBUTs7Ozs7O3dCQUtqQmpCLEtBQUtNLFVBQVUsSUFBSWhCLGdCQUFnQkcsdUJBQ2xDLDhEQUFDTixrRUFBTUE7NEJBQ0wrQixTQUFTO2dDQUFFQyxTQUFTO2dDQUFHQyxHQUFHLENBQUM7NEJBQUc7NEJBQzlCQyxTQUFTO2dDQUFFRixTQUFTO2dDQUFHQyxHQUFHOzRCQUFFOzRCQUM1QkUsTUFBTTtnQ0FBRUgsU0FBUztnQ0FBR0MsR0FBRzs0QkFBRzs0QkFDMUJHLFlBQVk7Z0NBQUVDLFVBQVU7NEJBQUk7NEJBQzVCMUIsV0FBVTtzQ0FFViw0RUFBQ0Q7Z0NBQUdDLFdBQVU7MENBQ1hFLEtBQUtNLFVBQVUsQ0FBQ1AsR0FBRyxDQUFDLENBQUMwQixXQUFXQyx5QkFDL0IsOERBQUN6Qjt3Q0FBa0JILFdBQVU7OzBEQUMzQiw4REFBQ0k7Z0RBQUVDLE1BQU1zQixVQUFVckIsSUFBSTtnREFBRU4sV0FBVTswREFDaEMyQixVQUFVcEIsS0FBSzs7Ozs7OzRDQUVqQm9CLFVBQVVqQixXQUFXLGtCQUNwQiw4REFBQ0M7Z0RBQUVYLFdBQVU7MERBQXlCMkIsVUFBVWpCLFdBQVc7Ozs7Ozs0Q0FFNURpQixVQUFVZixLQUFLLGtCQUNkLDhEQUFDQztnREFDQ0MsS0FBS2EsVUFBVWYsS0FBSztnREFDcEJHLEtBQUtZLFVBQVVwQixLQUFLO2dEQUNwQlAsV0FBVTs7Ozs7Ozt1Q0FYUDRCOzs7Ozs7Ozs7Ozs7Ozs7O21CQW5DWmpDOzs7Ozs7Ozs7Ozs7Ozs7QUEyRGpCO0dBbEdNTDtLQUFBQTtBQW9HTixpRUFBZUEsY0FBY0EsRUFBQyIsInNvdXJjZXMiOlsiL2NvZGUvc3JjL2xheW91dHMvaGVhZGVyL2NvbXBvbmVudHMvbmF2L05hdmlnYXRpb25NZW51LnRzeCJdLCJzb3VyY2VzQ29udGVudCI6WyJcInVzZSBjbGllbnRcIlxuaW1wb3J0IFJlYWN0LCB7IHVzZVN0YXRlIH0gZnJvbSAncmVhY3QnO1xuaW1wb3J0IE1vdGlvbiBmcm9tICdAL2NvbXBvbmVudHMvbW90aW9ucy9Nb3Rpb24nO1xuXG5pbnRlcmZhY2UgU3ViT3B0aW9uIHtcbiAgbGFiZWw6IHN0cmluZztcbiAgbGluazogc3RyaW5nO1xuICBkZXNjcmlwdGlvbj86IHN0cmluZztcbiAgaW1hZ2U/OiBzdHJpbmc7XG59XG5cbmludGVyZmFjZSBOYXZpZ2F0aW9uSXRlbSB7XG4gIGxhYmVsOiBzdHJpbmc7XG4gIGxpbms6IHN0cmluZztcbiAgc3ViT3B0aW9ucz86IFN1Yk9wdGlvbltdO1xuICBtZWdhTWVudT86IEpTWC5FbGVtZW50OyAgLy8gRm9yIHRoZSBtZWdhIG1lbnUgY29udGVudFxufVxuXG5pbnRlcmZhY2UgTmF2aWdhdGlvbk1lbnVQcm9wcyB7XG4gIG1lbnVJdGVtczogTmF2aWdhdGlvbkl0ZW1bXTtcbn1cblxuY29uc3QgTmF2aWdhdGlvbk1lbnU6IFJlYWN0LkZDPE5hdmlnYXRpb25NZW51UHJvcHM+ID0gKHsgbWVudUl0ZW1zIH0pID0+IHtcbiAgY29uc3QgW2FjdGl2ZUluZGV4LCBzZXRBY3RpdmVJbmRleF0gPSB1c2VTdGF0ZTxudW1iZXIgfCBudWxsPihudWxsKTtcblxuICBjb25zdCBoYW5kbGVNb3VzZUVudGVyID0gKGluZGV4OiBudW1iZXIpID0+IHtcbiAgICBzZXRBY3RpdmVJbmRleChpbmRleCk7XG4gIH07XG5cbiAgY29uc3QgaGFuZGxlTW91c2VMZWF2ZSA9ICgpID0+IHtcbiAgICBzZXRBY3RpdmVJbmRleChudWxsKTtcbiAgfTtcblxuICBjb25zdCByZW5kZXJNZW51SXRlbXMgPSAoaXRlbXM6IFN1Yk9wdGlvbltdKSA9PiB7XG4gICAgcmV0dXJuIChcbiAgICAgIDx1bCBjbGFzc05hbWU9XCJzcGFjZS15LTJcIj5cbiAgICAgICAge2l0ZW1zLm1hcCgoaXRlbSwgaW5kZXgpID0+IChcbiAgICAgICAgICA8bGkga2V5PXtpbmRleH0gY2xhc3NOYW1lPVwiaG92ZXI6YmctZ3JheS03MDAgcm91bmRlZC1tZCBwLTJcIj5cbiAgICAgICAgICAgIDxhIGhyZWY9e2l0ZW0ubGlua30gY2xhc3NOYW1lPVwiYmxvY2sgdGV4dC13aGl0ZVwiPlxuICAgICAgICAgICAgICB7aXRlbS5sYWJlbH1cbiAgICAgICAgICAgIDwvYT5cbiAgICAgICAgICAgIHsvKiBJZiB0aGUgaXRlbSBoYXMgc3ViT3B0aW9ucywgcmVuZGVyIHRoZW0gcmVjdXJzaXZlbHkgKi99XG4gICAgICAgICAgICB7aXRlbS5zdWJPcHRpb25zICYmIChcbiAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJwbC00XCI+XG4gICAgICAgICAgICAgICAge3JlbmRlck1lbnVJdGVtcyhpdGVtLnN1Yk9wdGlvbnMpfSB7LyogUmVjdXJzaXZlIHJlbmRlcmluZyAqL31cbiAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICApfVxuICAgICAgICAgICAgey8qIE9wdGlvbmFsIGltYWdlIGFuZCBkZXNjcmlwdGlvbiAqL31cbiAgICAgICAgICAgIHtpdGVtLmRlc2NyaXB0aW9uICYmIDxwIGNsYXNzTmFtZT1cInRleHQtc20gdGV4dC1ncmF5LTQwMFwiPntpdGVtLmRlc2NyaXB0aW9ufTwvcD59XG4gICAgICAgICAgICB7aXRlbS5pbWFnZSAmJiA8aW1nIHNyYz17aXRlbS5pbWFnZX0gYWx0PXtpdGVtLmxhYmVsfSBjbGFzc05hbWU9XCJ3LTE2IGgtYXV0byBtdC0yIHJvdW5kZWQtbWRcIiAvPn1cbiAgICAgICAgICA8L2xpPlxuICAgICAgICApKX1cbiAgICAgIDwvdWw+XG4gICAgKTtcbiAgfTtcblxuICByZXR1cm4gKFxuICAgIDxuYXYgY2xhc3NOYW1lPVwidy1mdWxsIGZsZXgganVzdGlmeS1jZW50ZXJcIj5cbiAgICAgIDx1bCBjbGFzc05hbWU9XCJmbGV4IGdhcC0xMlwiPlxuICAgICAgICB7bWVudUl0ZW1zLm1hcCgoaXRlbSwgaW5kZXgpID0+IChcbiAgICAgICAgICA8bGlcbiAgICAgICAgICAgIGtleT17aW5kZXh9XG4gICAgICAgICAgICBjbGFzc05hbWU9XCJyZWxhdGl2ZSBncm91cFwiXG4gICAgICAgICAgICBvbk1vdXNlRW50ZXI9eygpID0+IGhhbmRsZU1vdXNlRW50ZXIoaW5kZXgpfVxuICAgICAgICAgICAgb25Nb3VzZUxlYXZlPXtoYW5kbGVNb3VzZUxlYXZlfVxuICAgICAgICAgID5cbiAgICAgICAgICAgIDxhXG4gICAgICAgICAgICAgIGhyZWY9e2l0ZW0ubGlua31cbiAgICAgICAgICAgICAgY2xhc3NOYW1lPVwidGV4dC13aGl0ZSB0ZXh0LWxnIGZvbnQtc2VtaWJvbGQgaG92ZXI6dGV4dC1ibHVlLTUwMCB0cmFuc2l0aW9uLWFsbFwiXG4gICAgICAgICAgICA+XG4gICAgICAgICAgICAgIHtpdGVtLmxhYmVsfVxuICAgICAgICAgICAgPC9hPlxuXG4gICAgICAgICAgICB7aXRlbS5tZWdhTWVudSAmJiBhY3RpdmVJbmRleCA9PT0gaW5kZXggJiYgKFxuICAgICAgICAgICAgICA8TW90aW9uXG4gICAgICAgICAgICAgICAgaW5pdGlhbD17eyBvcGFjaXR5OiAwLCB5OiAtMTAgfX1cbiAgICAgICAgICAgICAgICBhbmltYXRlPXt7IG9wYWNpdHk6IDEsIHk6IDAgfX1cbiAgICAgICAgICAgICAgICBleGl0PXt7IG9wYWNpdHk6IDAsIHk6IDEwIH19XG4gICAgICAgICAgICAgICAgdHJhbnNpdGlvbj17eyBkdXJhdGlvbjogMC4zIH19XG4gICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwiYWJzb2x1dGUgdG9wLWZ1bGwgbGVmdC0wIHctZnVsbCBiZy1ncmF5LTkwMCBwLTYgZ3JpZCBncmlkLWNvbHMtNCBnYXAtNiB6LTEwXCJcbiAgICAgICAgICAgICAgPlxuICAgICAgICAgICAgICAgIHtpdGVtLm1lZ2FNZW51fVxuICAgICAgICAgICAgICA8L01vdGlvbj5cbiAgICAgICAgICAgICl9XG5cbiAgICAgICAgICAgIHsvKiBTdWJtZW51IERyb3Bkb3duIChOZXN0ZWQgaXRlbXMpICovfVxuICAgICAgICAgICAge2l0ZW0uc3ViT3B0aW9ucyAmJiBhY3RpdmVJbmRleCA9PT0gaW5kZXggJiYgKFxuICAgICAgICAgICAgICA8TW90aW9uXG4gICAgICAgICAgICAgICAgaW5pdGlhbD17eyBvcGFjaXR5OiAwLCB5OiAtMTAgfX1cbiAgICAgICAgICAgICAgICBhbmltYXRlPXt7IG9wYWNpdHk6IDEsIHk6IDAgfX1cbiAgICAgICAgICAgICAgICBleGl0PXt7IG9wYWNpdHk6IDAsIHk6IDEwIH19XG4gICAgICAgICAgICAgICAgdHJhbnNpdGlvbj17eyBkdXJhdGlvbjogMC4zIH19XG4gICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwiYWJzb2x1dGUgdG9wLWZ1bGwgbGVmdC0wIGJnLWdyYXktODAwIHRleHQtd2hpdGUgc2hhZG93LW1kIHJvdW5kZWQtbWQgei0xMFwiXG4gICAgICAgICAgICAgID5cbiAgICAgICAgICAgICAgICA8dWwgY2xhc3NOYW1lPVwic3BhY2UteS0yIHAtNFwiPlxuICAgICAgICAgICAgICAgICAge2l0ZW0uc3ViT3B0aW9ucy5tYXAoKHN1Yk9wdGlvbiwgc3ViSW5kZXgpID0+IChcbiAgICAgICAgICAgICAgICAgICAgPGxpIGtleT17c3ViSW5kZXh9IGNsYXNzTmFtZT1cImhvdmVyOmJnLWdyYXktNzAwIHJvdW5kZWQtbWQgcC0yXCI+XG4gICAgICAgICAgICAgICAgICAgICAgPGEgaHJlZj17c3ViT3B0aW9uLmxpbmt9IGNsYXNzTmFtZT1cImJsb2NrXCI+XG4gICAgICAgICAgICAgICAgICAgICAgICB7c3ViT3B0aW9uLmxhYmVsfVxuICAgICAgICAgICAgICAgICAgICAgIDwvYT5cbiAgICAgICAgICAgICAgICAgICAgICB7c3ViT3B0aW9uLmRlc2NyaXB0aW9uICYmIChcbiAgICAgICAgICAgICAgICAgICAgICAgIDxwIGNsYXNzTmFtZT1cInRleHQtc20gdGV4dC1ncmF5LTQwMFwiPntzdWJPcHRpb24uZGVzY3JpcHRpb259PC9wPlxuICAgICAgICAgICAgICAgICAgICAgICl9XG4gICAgICAgICAgICAgICAgICAgICAge3N1Yk9wdGlvbi5pbWFnZSAmJiAoXG4gICAgICAgICAgICAgICAgICAgICAgICA8aW1nXG4gICAgICAgICAgICAgICAgICAgICAgICAgIHNyYz17c3ViT3B0aW9uLmltYWdlfVxuICAgICAgICAgICAgICAgICAgICAgICAgICBhbHQ9e3N1Yk9wdGlvbi5sYWJlbH1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwidy0xNiBoLWF1dG8gbXQtMiByb3VuZGVkLW1kXCJcbiAgICAgICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgICAgICAgKX1cbiAgICAgICAgICAgICAgICAgICAgPC9saT5cbiAgICAgICAgICAgICAgICAgICkpfVxuICAgICAgICAgICAgICAgIDwvdWw+XG4gICAgICAgICAgICAgIDwvTW90aW9uPlxuICAgICAgICAgICAgKX1cbiAgICAgICAgICA8L2xpPlxuICAgICAgICApKX1cbiAgICAgIDwvdWw+XG4gICAgPC9uYXY+XG4gICk7XG59O1xuXG5leHBvcnQgZGVmYXVsdCBOYXZpZ2F0aW9uTWVudTtcbiJdLCJuYW1lcyI6WyJSZWFjdCIsInVzZVN0YXRlIiwiTW90aW9uIiwiTmF2aWdhdGlvbk1lbnUiLCJtZW51SXRlbXMiLCJhY3RpdmVJbmRleCIsInNldEFjdGl2ZUluZGV4IiwiaGFuZGxlTW91c2VFbnRlciIsImluZGV4IiwiaGFuZGxlTW91c2VMZWF2ZSIsInJlbmRlck1lbnVJdGVtcyIsIml0ZW1zIiwidWwiLCJjbGFzc05hbWUiLCJtYXAiLCJpdGVtIiwibGkiLCJhIiwiaHJlZiIsImxpbmsiLCJsYWJlbCIsInN1Yk9wdGlvbnMiLCJkaXYiLCJkZXNjcmlwdGlvbiIsInAiLCJpbWFnZSIsImltZyIsInNyYyIsImFsdCIsIm5hdiIsIm9uTW91c2VFbnRlciIsIm9uTW91c2VMZWF2ZSIsIm1lZ2FNZW51IiwiaW5pdGlhbCIsIm9wYWNpdHkiLCJ5IiwiYW5pbWF0ZSIsImV4aXQiLCJ0cmFuc2l0aW9uIiwiZHVyYXRpb24iLCJzdWJPcHRpb24iLCJzdWJJbmRleCJdLCJpZ25vcmVMaXN0IjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/layouts/header/components/nav/NavigationMenu.tsx\n"));

/***/ })

});
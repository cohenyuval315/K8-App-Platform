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

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/components/motions/Motion */ \"(app-pages-browser)/./src/components/motions/Motion.tsx\");\n/* __next_internal_client_entry_do_not_use__ default auto */ \nvar _s = $RefreshSig$();\n\n\nconst NavigationMenuLink = (param)=>{\n    let { label, link } = param;\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n        className: \"relative\" // Wrapper div to position text and background properly\n        ,\n        // whileHover={{ scale: 1.05 }}\n        transition: {\n            duration: 0.3\n        },\n        children: [\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n                className: \"absolute inset-0 bg-gray-800 opacity-0 rounded-md\" // Background div (initial opacity 0)\n                ,\n                whileHover: {\n                    opacity: 0.5\n                },\n                transition: {\n                    opacity: {\n                        duration: 0.5\n                    }\n                }\n            }, void 0, false, {\n                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                lineNumber: 37,\n                columnNumber: 7\n            }, undefined),\n            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n                type: \"a\",\n                href: link ? link : \"/\",\n                className: \"text-white text-lg font-semibold hover:text-blue-500 transition-all relative z-10\",\n                children: label\n            }, void 0, false, {\n                fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                lineNumber: 42,\n                columnNumber: 7\n            }, undefined)\n        ]\n    }, void 0, true, {\n        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n        lineNumber: 32,\n        columnNumber: 5\n    }, undefined);\n};\n_c = NavigationMenuLink;\nconst NavigationMenu = (param)=>{\n    let { menuItems } = param;\n    _s();\n    const [activeIndex, setActiveIndex] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(null);\n    const handleMouseEnter = (index)=>{\n        setActiveIndex(index);\n    };\n    const handleMouseLeave = ()=>{\n        setActiveIndex(null);\n    };\n    const renderMenuItems = (items, rows)=>{\n        const className = rows ? \"space-x-1\" : \"flex space-x-\".concat(items.length);\n        return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"ul\", {\n            className: className,\n            children: items.map((item, index)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"li\", {\n                    children: [\n                        item.link ? /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(NavigationMenuLink, {\n                            label: item.label,\n                            link: item.link\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 74,\n                            columnNumber: 15\n                        }, undefined) : /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                            className: \"text-sm text-gray-400\",\n                            children: item.label\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 79,\n                            columnNumber: 15\n                        }, undefined),\n                        item.description && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"p\", {\n                            className: \"text-sm text-gray-400\",\n                            children: item.description\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 83,\n                            columnNumber: 34\n                        }, undefined),\n                        item.subOptions && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                            className: \"\",\n                            children: renderMenuItems(item.subOptions, item.rows)\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 86,\n                            columnNumber: 15\n                        }, undefined)\n                    ]\n                }, index, true, {\n                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                    lineNumber: 72,\n                    columnNumber: 11\n                }, undefined))\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n            lineNumber: 70,\n            columnNumber: 7\n        }, undefined);\n    };\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"nav\", {\n        className: \"w-full flex justify-center\",\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"ul\", {\n            className: \"flex gap-12\",\n            children: menuItems.map((item, index)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"li\", {\n                    className: \"relative group\",\n                    onMouseEnter: ()=>handleMouseEnter(index),\n                    onMouseLeave: handleMouseLeave,\n                    children: [\n                        /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(NavigationMenuLink, {\n                            label: item.label,\n                            link: item.link\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 109,\n                            columnNumber: 13\n                        }, undefined),\n                        item.subOptions && activeIndex === index && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n                            initial: {\n                                opacity: 0,\n                                y: -10\n                            },\n                            animate: {\n                                opacity: 1,\n                                y: 0\n                            },\n                            exit: {\n                                opacity: 0,\n                                y: 10\n                            },\n                            transition: {\n                                duration: 0.3\n                            },\n                            className: \"absolute top-full left-0\",\n                            children: renderMenuItems(item.subOptions, item.rows)\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 115,\n                            columnNumber: 15\n                        }, undefined)\n                    ]\n                }, index, true, {\n                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                    lineNumber: 102,\n                    columnNumber: 11\n                }, undefined))\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n            lineNumber: 100,\n            columnNumber: 7\n        }, undefined)\n    }, void 0, false, {\n        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n        lineNumber: 99,\n        columnNumber: 5\n    }, undefined);\n};\n_s(NavigationMenu, \"E8kOn+IkK/htiBGEqJWkEvOqULU=\");\n_c1 = NavigationMenu;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (NavigationMenu);\nvar _c, _c1;\n$RefreshReg$(_c, \"NavigationMenuLink\");\n$RefreshReg$(_c1, \"NavigationMenu\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9sYXlvdXRzL2hlYWRlci9jb21wb25lbnRzL25hdi9OYXZpZ2F0aW9uTWVudS50c3giLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7OztBQUN3QztBQUNTO0FBMEJqRCxNQUFNRyxxQkFBbUQ7UUFBQyxFQUFDQyxLQUFLLEVBQUVDLElBQUksRUFBQztJQUNyRSxxQkFFRSw4REFBQ0gsa0VBQU1BO1FBQ0xJLFdBQVUsV0FBVyx1REFBdUQ7O1FBQzVFLCtCQUErQjtRQUMvQkMsWUFBWTtZQUFFQyxVQUFVO1FBQUk7OzBCQUU1Qiw4REFBQ04sa0VBQU1BO2dCQUNMSSxXQUFVLG9EQUFvRCxxQ0FBcUM7O2dCQUNuR0csWUFBWTtvQkFBRUMsU0FBUztnQkFBSTtnQkFDM0JILFlBQVk7b0JBQUVHLFNBQVM7d0JBQUVGLFVBQVU7b0JBQUk7Z0JBQUU7Ozs7OzswQkFFM0MsOERBQUNOLGtFQUFNQTtnQkFDTFMsTUFBSztnQkFDTEMsTUFBTVAsT0FBT0EsT0FBTztnQkFDcEJDLFdBQVU7MEJBSVRGOzs7Ozs7Ozs7Ozs7QUFLVDtLQXpCTUQ7QUEyQk4sTUFBTVUsaUJBQWdEO1FBQUMsRUFBRUMsU0FBUyxFQUFFOztJQUNsRSxNQUFNLENBQUNDLGFBQWFDLGVBQWUsR0FBR2YsK0NBQVFBLENBQWdCO0lBRTlELE1BQU1nQixtQkFBbUIsQ0FBQ0M7UUFDeEJGLGVBQWVFO0lBQ2pCO0lBRUEsTUFBTUMsbUJBQW1CO1FBQ3ZCSCxlQUFlO0lBQ2pCO0lBRUEsTUFBTUksa0JBQWtCLENBQUNDLE9BQW9CQztRQUMzQyxNQUFNaEIsWUFBWWdCLE9BQVEsY0FBYSxnQkFBNkIsT0FBYkQsTUFBTUUsTUFBTTtRQUNuRSxxQkFDRSw4REFBQ0M7WUFBR2xCLFdBQVdBO3NCQUNaZSxNQUFNSSxHQUFHLENBQUMsQ0FBQ0MsTUFBTVIsc0JBQ2hCLDhEQUFDUzs7d0JBQ0VELEtBQUtyQixJQUFJLGlCQUNSLDhEQUFDRjs0QkFDQ0MsT0FBT3NCLEtBQUt0QixLQUFLOzRCQUNqQkMsTUFBTXFCLEtBQUtyQixJQUFJOzs7OztzREFHakIsOERBQUN1Qjs0QkFBSXRCLFdBQVU7c0NBQ1pvQixLQUFLdEIsS0FBSzs7Ozs7O3dCQUdkc0IsS0FBS0csV0FBVyxrQkFBSSw4REFBQ0M7NEJBQUV4QixXQUFVO3NDQUF5Qm9CLEtBQUtHLFdBQVc7Ozs7Ozt3QkFFMUVILEtBQUtLLFVBQVUsa0JBQ2QsOERBQUNIOzRCQUFJdEIsV0FBVTtzQ0FDWmMsZ0JBQWdCTSxLQUFLSyxVQUFVLEVBQUVMLEtBQUtKLElBQUk7Ozs7Ozs7bUJBZnhDSjs7Ozs7Ozs7OztJQXNCakI7SUFJQSxxQkFDRSw4REFBQ2M7UUFBSTFCLFdBQVU7a0JBQ2IsNEVBQUNrQjtZQUFHbEIsV0FBVTtzQkFDWFEsVUFBVVcsR0FBRyxDQUFDLENBQUNDLE1BQU1SLHNCQUNwQiw4REFBQ1M7b0JBRUNyQixXQUFVO29CQUNWMkIsY0FBYyxJQUFNaEIsaUJBQWlCQztvQkFDckNnQixjQUFjZjs7c0NBR2QsOERBQUNoQjs0QkFDQ0MsT0FBT3NCLEtBQUt0QixLQUFLOzRCQUNqQkMsTUFBTXFCLEtBQUtyQixJQUFJOzs7Ozs7d0JBR2hCcUIsS0FBS0ssVUFBVSxJQUFJaEIsZ0JBQWdCRyx1QkFDbEMsOERBQUNoQixrRUFBTUE7NEJBQ0xpQyxTQUFTO2dDQUFFekIsU0FBUztnQ0FBRzBCLEdBQUcsQ0FBQzs0QkFBRzs0QkFDOUJDLFNBQVM7Z0NBQUUzQixTQUFTO2dDQUFHMEIsR0FBRzs0QkFBRTs0QkFDNUJFLE1BQU07Z0NBQUU1QixTQUFTO2dDQUFHMEIsR0FBRzs0QkFBRzs0QkFDMUI3QixZQUFZO2dDQUFFQyxVQUFVOzRCQUFJOzRCQUM1QkYsV0FBVTtzQ0FFVGMsZ0JBQWdCTSxLQUFLSyxVQUFVLEVBQUVMLEtBQUtKLElBQUk7Ozs7Ozs7bUJBbkIxQ0o7Ozs7Ozs7Ozs7Ozs7OztBQTRCakI7R0EzRU1MO01BQUFBO0FBNkVOLGlFQUFlQSxjQUFjQSxFQUFDIiwic291cmNlcyI6WyIvY29kZS9zcmMvbGF5b3V0cy9oZWFkZXIvY29tcG9uZW50cy9uYXYvTmF2aWdhdGlvbk1lbnUudHN4Il0sInNvdXJjZXNDb250ZW50IjpbIlwidXNlIGNsaWVudFwiXG5pbXBvcnQgUmVhY3QsIHsgdXNlU3RhdGUgfSBmcm9tICdyZWFjdCc7XG5pbXBvcnQgTW90aW9uIGZyb20gJ0AvY29tcG9uZW50cy9tb3Rpb25zL01vdGlvbic7XG5cbmludGVyZmFjZSBTdWJPcHRpb24ge1xuICBsYWJlbDogc3RyaW5nO1xuICBsaW5rOiBzdHJpbmc7XG4gIGRlc2NyaXB0aW9uPzogc3RyaW5nO1xuICByb3dzOmJvb2xlYW47XG4gIHN1Yk9wdGlvbnM/OiBTdWJPcHRpb25bXTtcbn1cblxuaW50ZXJmYWNlIE5hdmlnYXRpb25JdGVtIHtcbiAgbGFiZWw6IHN0cmluZztcbiAgbGluaz86IHN0cmluZztcbiAgcm93czpib29sZWFuO1xuICBzdWJPcHRpb25zPzogU3ViT3B0aW9uW107XG59XG5cbmludGVyZmFjZSBOYXZpZ2F0aW9uTWVudVByb3BzIHtcbiAgbWVudUl0ZW1zOiBOYXZpZ2F0aW9uSXRlbVtdO1xufVxuXG5pbnRlcmZhY2UgTmF2aWdhdGlvbk1lbnVMaW5rIHtcbiAgbGFiZWw6c3RyaW5nO1xuICBsaW5rPzpzdHJpbmc7XG59XG5cbmNvbnN0IE5hdmlnYXRpb25NZW51TGluazpSZWFjdC5GQzxOYXZpZ2F0aW9uTWVudUxpbms+ICA9ICh7bGFiZWwsIGxpbmt9KSA9PiB7XG4gIHJldHVybiAoXG5cbiAgICA8TW90aW9uXG4gICAgICBjbGFzc05hbWU9XCJyZWxhdGl2ZVwiIC8vIFdyYXBwZXIgZGl2IHRvIHBvc2l0aW9uIHRleHQgYW5kIGJhY2tncm91bmQgcHJvcGVybHlcbiAgICAgIC8vIHdoaWxlSG92ZXI9e3sgc2NhbGU6IDEuMDUgfX1cbiAgICAgIHRyYW5zaXRpb249e3sgZHVyYXRpb246IDAuMyB9fVxuICAgID5cbiAgICAgIDxNb3Rpb25cbiAgICAgICAgY2xhc3NOYW1lPVwiYWJzb2x1dGUgaW5zZXQtMCBiZy1ncmF5LTgwMCBvcGFjaXR5LTAgcm91bmRlZC1tZFwiIC8vIEJhY2tncm91bmQgZGl2IChpbml0aWFsIG9wYWNpdHkgMClcbiAgICAgICAgd2hpbGVIb3Zlcj17eyBvcGFjaXR5OiAwLjUgfX0gLy8gT24gaG92ZXIsIGJhY2tncm91bmQgb3BhY2l0eSB3aWxsIGNoYW5nZSB0byAwLjVcbiAgICAgICAgdHJhbnNpdGlvbj17eyBvcGFjaXR5OiB7IGR1cmF0aW9uOiAwLjUgfSB9fSAvLyBTbW9vdGggdHJhbnNpdGlvbiBvZiBvcGFjaXR5XG4gICAgICAvPlxuICAgICAgPE1vdGlvblxuICAgICAgICB0eXBlPSdhJ1xuICAgICAgICBocmVmPXtsaW5rID8gbGluayA6IFwiL1wifVxuICAgICAgICBjbGFzc05hbWU9XCJ0ZXh0LXdoaXRlIHRleHQtbGcgZm9udC1zZW1pYm9sZCBob3Zlcjp0ZXh0LWJsdWUtNTAwIHRyYW5zaXRpb24tYWxsIHJlbGF0aXZlIHotMTBcIlxuICAgICAgICAvLyB3aGlsZUhvdmVyPXt7IHNjYWxlOiAxLjEgfX1cbiAgICAgICAgLy8gdHJhbnNpdGlvbj17eyBkdXJhdGlvbjogMC41IH19XG4gICAgICA+XG4gICAgICAgIHtsYWJlbH1cbiAgICAgIDwvTW90aW9uPlxuICAgIDwvTW90aW9uPlxuXG4gIClcbn1cblxuY29uc3QgTmF2aWdhdGlvbk1lbnU6IFJlYWN0LkZDPE5hdmlnYXRpb25NZW51UHJvcHM+ID0gKHsgbWVudUl0ZW1zIH0pID0+IHtcbiAgY29uc3QgW2FjdGl2ZUluZGV4LCBzZXRBY3RpdmVJbmRleF0gPSB1c2VTdGF0ZTxudW1iZXIgfCBudWxsPihudWxsKTtcblxuICBjb25zdCBoYW5kbGVNb3VzZUVudGVyID0gKGluZGV4OiBudW1iZXIpID0+IHtcbiAgICBzZXRBY3RpdmVJbmRleChpbmRleCk7XG4gIH07XG5cbiAgY29uc3QgaGFuZGxlTW91c2VMZWF2ZSA9ICgpID0+IHtcbiAgICBzZXRBY3RpdmVJbmRleChudWxsKTtcbiAgfTtcblxuICBjb25zdCByZW5kZXJNZW51SXRlbXMgPSAoaXRlbXM6IFN1Yk9wdGlvbltdLCByb3dzOmJvb2xlYW4pID0+IHtcbiAgICBjb25zdCBjbGFzc05hbWUgPSByb3dzID8gYHNwYWNlLXgtMWAgOiBgZmxleCBzcGFjZS14LSR7aXRlbXMubGVuZ3RofWBcbiAgICByZXR1cm4gKFxuICAgICAgPHVsIGNsYXNzTmFtZT17Y2xhc3NOYW1lfT5cbiAgICAgICAge2l0ZW1zLm1hcCgoaXRlbSwgaW5kZXgpID0+IChcbiAgICAgICAgICA8bGkga2V5PXtpbmRleH0+XG4gICAgICAgICAgICB7aXRlbS5saW5rID8gKFxuICAgICAgICAgICAgICA8TmF2aWdhdGlvbk1lbnVMaW5rXG4gICAgICAgICAgICAgICAgbGFiZWw9e2l0ZW0ubGFiZWx9XG4gICAgICAgICAgICAgICAgbGluaz17aXRlbS5saW5rfVxuICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgKTogKFxuICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT0ndGV4dC1zbSB0ZXh0LWdyYXktNDAwJz5cbiAgICAgICAgICAgICAgICB7aXRlbS5sYWJlbH1cbiAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICApfVxuICAgICAgICAgICAge2l0ZW0uZGVzY3JpcHRpb24gJiYgPHAgY2xhc3NOYW1lPVwidGV4dC1zbSB0ZXh0LWdyYXktNDAwXCI+e2l0ZW0uZGVzY3JpcHRpb259PC9wPn1cblxuICAgICAgICAgICAge2l0ZW0uc3ViT3B0aW9ucyAmJiAoXG4gICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiXCI+XG4gICAgICAgICAgICAgICAge3JlbmRlck1lbnVJdGVtcyhpdGVtLnN1Yk9wdGlvbnMsIGl0ZW0ucm93cyl9XG4gICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgKX1cbiAgICAgICAgICA8L2xpPlxuICAgICAgICApKX1cbiAgICAgIDwvdWw+XG4gICAgKTtcbiAgfTtcblxuXG5cbiAgcmV0dXJuIChcbiAgICA8bmF2IGNsYXNzTmFtZT1cInctZnVsbCBmbGV4IGp1c3RpZnktY2VudGVyXCI+XG4gICAgICA8dWwgY2xhc3NOYW1lPVwiZmxleCBnYXAtMTJcIj5cbiAgICAgICAge21lbnVJdGVtcy5tYXAoKGl0ZW0sIGluZGV4KSA9PiAoXG4gICAgICAgICAgPGxpXG4gICAgICAgICAgICBrZXk9e2luZGV4fVxuICAgICAgICAgICAgY2xhc3NOYW1lPVwicmVsYXRpdmUgZ3JvdXBcIlxuICAgICAgICAgICAgb25Nb3VzZUVudGVyPXsoKSA9PiBoYW5kbGVNb3VzZUVudGVyKGluZGV4KX1cbiAgICAgICAgICAgIG9uTW91c2VMZWF2ZT17aGFuZGxlTW91c2VMZWF2ZX1cbiAgICAgICAgICA+XG5cbiAgICAgICAgICAgIDxOYXZpZ2F0aW9uTWVudUxpbmtcbiAgICAgICAgICAgICAgbGFiZWw9e2l0ZW0ubGFiZWx9XG4gICAgICAgICAgICAgIGxpbms9e2l0ZW0ubGlua31cbiAgICAgICAgICAgIC8+XG5cbiAgICAgICAgICAgIHtpdGVtLnN1Yk9wdGlvbnMgJiYgYWN0aXZlSW5kZXggPT09IGluZGV4ICYmIChcbiAgICAgICAgICAgICAgPE1vdGlvblxuICAgICAgICAgICAgICAgIGluaXRpYWw9e3sgb3BhY2l0eTogMCwgeTogLTEwIH19XG4gICAgICAgICAgICAgICAgYW5pbWF0ZT17eyBvcGFjaXR5OiAxLCB5OiAwIH19XG4gICAgICAgICAgICAgICAgZXhpdD17eyBvcGFjaXR5OiAwLCB5OiAxMCB9fVxuICAgICAgICAgICAgICAgIHRyYW5zaXRpb249e3sgZHVyYXRpb246IDAuMyB9fVxuICAgICAgICAgICAgICAgIGNsYXNzTmFtZT1cImFic29sdXRlIHRvcC1mdWxsIGxlZnQtMFwiXG4gICAgICAgICAgICAgID5cbiAgICAgICAgICAgICAgICB7cmVuZGVyTWVudUl0ZW1zKGl0ZW0uc3ViT3B0aW9ucywgaXRlbS5yb3dzKX1cbiAgICAgICAgICAgICAgPC9Nb3Rpb24+XG4gICAgICAgICAgICApfVxuXG4gICAgICAgICAgPC9saT5cbiAgICAgICAgKSl9XG4gICAgICA8L3VsPlxuICAgIDwvbmF2PlxuICApO1xufTtcblxuZXhwb3J0IGRlZmF1bHQgTmF2aWdhdGlvbk1lbnU7XG4iXSwibmFtZXMiOlsiUmVhY3QiLCJ1c2VTdGF0ZSIsIk1vdGlvbiIsIk5hdmlnYXRpb25NZW51TGluayIsImxhYmVsIiwibGluayIsImNsYXNzTmFtZSIsInRyYW5zaXRpb24iLCJkdXJhdGlvbiIsIndoaWxlSG92ZXIiLCJvcGFjaXR5IiwidHlwZSIsImhyZWYiLCJOYXZpZ2F0aW9uTWVudSIsIm1lbnVJdGVtcyIsImFjdGl2ZUluZGV4Iiwic2V0QWN0aXZlSW5kZXgiLCJoYW5kbGVNb3VzZUVudGVyIiwiaW5kZXgiLCJoYW5kbGVNb3VzZUxlYXZlIiwicmVuZGVyTWVudUl0ZW1zIiwiaXRlbXMiLCJyb3dzIiwibGVuZ3RoIiwidWwiLCJtYXAiLCJpdGVtIiwibGkiLCJkaXYiLCJkZXNjcmlwdGlvbiIsInAiLCJzdWJPcHRpb25zIiwibmF2Iiwib25Nb3VzZUVudGVyIiwib25Nb3VzZUxlYXZlIiwiaW5pdGlhbCIsInkiLCJhbmltYXRlIiwiZXhpdCJdLCJpZ25vcmVMaXN0IjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/layouts/header/components/nav/NavigationMenu.tsx\n"));

/***/ })

});
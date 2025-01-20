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

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var _components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/components/motions/Motion */ \"(app-pages-browser)/./src/components/motions/Motion.tsx\");\n/* __next_internal_client_entry_do_not_use__ default auto */ \nvar _s = $RefreshSig$();\n\n\nconst NavigationMenuLink = (param)=>{\n    let { label, link } = param;\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n        type: \"a\",\n        href: link ? link : \"/\",\n        className: \"text-white text-lg font-semibold hover:text-blue-500 transition-all\",\n        children: label\n    }, void 0, false, {\n        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n        lineNumber: 29,\n        columnNumber: 5\n    }, undefined);\n};\n_c = NavigationMenuLink;\nconst NavigationMenu = (param)=>{\n    let { menuItems } = param;\n    _s();\n    const [activeIndex, setActiveIndex] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(null);\n    const handleMouseEnter = (index)=>{\n        setActiveIndex(index);\n    };\n    const handleMouseLeave = ()=>{\n        setActiveIndex(null);\n    };\n    const renderMenuItems = (items)=>{\n        return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"ul\", {\n            style: {\n                flexDirection: \"row\"\n            },\n            children: items.map((item, index)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"li\", {\n                    className: \"hover:bg-gray-700 rounded-md p-2\",\n                    children: [\n                        item.link ? /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(NavigationMenuLink, {\n                            label: item.label,\n                            link: item.link\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 60,\n                            columnNumber: 15\n                        }, undefined) : /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                            children: item.label\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 65,\n                            columnNumber: 15\n                        }, undefined),\n                        item.description && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"p\", {\n                            className: \"text-sm text-gray-400\",\n                            children: item.description\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 69,\n                            columnNumber: 34\n                        }, undefined),\n                        item.subOptions && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                            className: \"pl-4\",\n                            children: renderMenuItems(item.subOptions)\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 72,\n                            columnNumber: 15\n                        }, undefined)\n                    ]\n                }, index, true, {\n                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                    lineNumber: 58,\n                    columnNumber: 11\n                }, undefined))\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n            lineNumber: 54,\n            columnNumber: 7\n        }, undefined);\n    };\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"nav\", {\n        className: \"w-full flex justify-center\",\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"ul\", {\n            className: \"flex gap-12\",\n            children: menuItems.map((item, index)=>/*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"li\", {\n                    className: \"relative group\",\n                    onMouseEnter: ()=>handleMouseEnter(index),\n                    onMouseLeave: handleMouseLeave,\n                    children: [\n                        /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(NavigationMenuLink, {\n                            label: item.label,\n                            link: item.link\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 95,\n                            columnNumber: 13\n                        }, undefined),\n                        item.subOptions && activeIndex === index && /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_motions_Motion__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n                            initial: {\n                                opacity: 0,\n                                y: -10\n                            },\n                            animate: {\n                                opacity: 1,\n                                y: 0\n                            },\n                            exit: {\n                                opacity: 0,\n                                y: 10\n                            },\n                            transition: {\n                                duration: 0.3\n                            },\n                            children: renderMenuItems(item.subOptions)\n                        }, void 0, false, {\n                            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                            lineNumber: 101,\n                            columnNumber: 15\n                        }, undefined)\n                    ]\n                }, index, true, {\n                    fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n                    lineNumber: 88,\n                    columnNumber: 11\n                }, undefined))\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n            lineNumber: 86,\n            columnNumber: 7\n        }, undefined)\n    }, void 0, false, {\n        fileName: \"/code/src/layouts/header/components/nav/NavigationMenu.tsx\",\n        lineNumber: 85,\n        columnNumber: 5\n    }, undefined);\n};\n_s(NavigationMenu, \"E8kOn+IkK/htiBGEqJWkEvOqULU=\");\n_c1 = NavigationMenu;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (NavigationMenu);\nvar _c, _c1;\n$RefreshReg$(_c, \"NavigationMenuLink\");\n$RefreshReg$(_c1, \"NavigationMenu\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9sYXlvdXRzL2hlYWRlci9jb21wb25lbnRzL25hdi9OYXZpZ2F0aW9uTWVudS50c3giLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7OztBQUN3QztBQUNTO0FBd0JqRCxNQUFNRyxxQkFBbUQ7UUFBQyxFQUFDQyxLQUFLLEVBQUVDLElBQUksRUFBQztJQUNyRSxxQkFDRSw4REFBQ0gsa0VBQU1BO1FBQ0xJLE1BQUs7UUFDTEMsTUFBTUYsT0FBT0EsT0FBTztRQUNwQkcsV0FBVTtrQkFJVEo7Ozs7OztBQUdQO0tBWk1EO0FBY04sTUFBTU0saUJBQWdEO1FBQUMsRUFBRUMsU0FBUyxFQUFFOztJQUNsRSxNQUFNLENBQUNDLGFBQWFDLGVBQWUsR0FBR1gsK0NBQVFBLENBQWdCO0lBRTlELE1BQU1ZLG1CQUFtQixDQUFDQztRQUN4QkYsZUFBZUU7SUFDakI7SUFFQSxNQUFNQyxtQkFBbUI7UUFDdkJILGVBQWU7SUFDakI7SUFFQSxNQUFNSSxrQkFBa0IsQ0FBQ0M7UUFDdkIscUJBQ0UsOERBQUNDO1lBQUdDLE9BQU87Z0JBQ1RDLGVBQWM7WUFDaEI7c0JBQ0dILE1BQU1JLEdBQUcsQ0FBQyxDQUFDQyxNQUFNUixzQkFDaEIsOERBQUNTO29CQUFlZixXQUFVOzt3QkFDdkJjLEtBQUtqQixJQUFJLGlCQUNSLDhEQUFDRjs0QkFDQ0MsT0FBT2tCLEtBQUtsQixLQUFLOzRCQUNqQkMsTUFBTWlCLEtBQUtqQixJQUFJOzs7OztzREFHakIsOERBQUNtQjtzQ0FDRUYsS0FBS2xCLEtBQUs7Ozs7Ozt3QkFHZGtCLEtBQUtHLFdBQVcsa0JBQUksOERBQUNDOzRCQUFFbEIsV0FBVTtzQ0FBeUJjLEtBQUtHLFdBQVc7Ozs7Ozt3QkFFMUVILEtBQUtLLFVBQVUsa0JBQ2QsOERBQUNIOzRCQUFJaEIsV0FBVTtzQ0FDWlEsZ0JBQWdCTSxLQUFLSyxVQUFVOzs7Ozs7O21CQWY3QmI7Ozs7Ozs7Ozs7SUFzQmpCO0lBSUEscUJBQ0UsOERBQUNjO1FBQUlwQixXQUFVO2tCQUNiLDRFQUFDVTtZQUFHVixXQUFVO3NCQUNYRSxVQUFVVyxHQUFHLENBQUMsQ0FBQ0MsTUFBTVIsc0JBQ3BCLDhEQUFDUztvQkFFQ2YsV0FBVTtvQkFDVnFCLGNBQWMsSUFBTWhCLGlCQUFpQkM7b0JBQ3JDZ0IsY0FBY2Y7O3NDQUdkLDhEQUFDWjs0QkFDQ0MsT0FBT2tCLEtBQUtsQixLQUFLOzRCQUNqQkMsTUFBTWlCLEtBQUtqQixJQUFJOzs7Ozs7d0JBR2hCaUIsS0FBS0ssVUFBVSxJQUFJaEIsZ0JBQWdCRyx1QkFDbEMsOERBQUNaLGtFQUFNQTs0QkFDTDZCLFNBQVM7Z0NBQUVDLFNBQVM7Z0NBQUdDLEdBQUcsQ0FBQzs0QkFBRzs0QkFDOUJDLFNBQVM7Z0NBQUVGLFNBQVM7Z0NBQUdDLEdBQUc7NEJBQUU7NEJBQzVCRSxNQUFNO2dDQUFFSCxTQUFTO2dDQUFHQyxHQUFHOzRCQUFHOzRCQUMxQkcsWUFBWTtnQ0FBRUMsVUFBVTs0QkFBSTtzQ0FHM0JyQixnQkFBZ0JNLEtBQUtLLFVBQVU7Ozs7Ozs7bUJBbkIvQmI7Ozs7Ozs7Ozs7Ozs7OztBQTRCakI7R0E1RU1MO01BQUFBO0FBOEVOLGlFQUFlQSxjQUFjQSxFQUFDIiwic291cmNlcyI6WyIvY29kZS9zcmMvbGF5b3V0cy9oZWFkZXIvY29tcG9uZW50cy9uYXYvTmF2aWdhdGlvbk1lbnUudHN4Il0sInNvdXJjZXNDb250ZW50IjpbIlwidXNlIGNsaWVudFwiXG5pbXBvcnQgUmVhY3QsIHsgdXNlU3RhdGUgfSBmcm9tICdyZWFjdCc7XG5pbXBvcnQgTW90aW9uIGZyb20gJ0AvY29tcG9uZW50cy9tb3Rpb25zL01vdGlvbic7XG5cbmludGVyZmFjZSBTdWJPcHRpb24ge1xuICBsYWJlbDogc3RyaW5nO1xuICBsaW5rOiBzdHJpbmc7XG4gIGRlc2NyaXB0aW9uPzogc3RyaW5nO1xuICBzdWJPcHRpb25zPzogU3ViT3B0aW9uW107IC8vIFN1cHBvcnQgZm9yIHJlY3Vyc2l2ZSBzdWJtZW51XG59XG5cbmludGVyZmFjZSBOYXZpZ2F0aW9uSXRlbSB7XG4gIGxhYmVsOiBzdHJpbmc7XG4gIGxpbms/OiBzdHJpbmc7XG4gIHN1Yk9wdGlvbnM/OiBTdWJPcHRpb25bXTtcbn1cblxuaW50ZXJmYWNlIE5hdmlnYXRpb25NZW51UHJvcHMge1xuICBtZW51SXRlbXM6IE5hdmlnYXRpb25JdGVtW107XG59XG5cbmludGVyZmFjZSBOYXZpZ2F0aW9uTWVudUxpbmsge1xuICBsYWJlbDpzdHJpbmc7XG4gIGxpbms/OnN0cmluZztcbn1cblxuY29uc3QgTmF2aWdhdGlvbk1lbnVMaW5rOlJlYWN0LkZDPE5hdmlnYXRpb25NZW51TGluaz4gID0gKHtsYWJlbCwgbGlua30pID0+IHtcbiAgcmV0dXJuIChcbiAgICA8TW90aW9uXG4gICAgICB0eXBlPSdhJ1xuICAgICAgaHJlZj17bGluayA/IGxpbmsgOiBcIi9cIn1cbiAgICAgIGNsYXNzTmFtZT1cInRleHQtd2hpdGUgdGV4dC1sZyBmb250LXNlbWlib2xkIGhvdmVyOnRleHQtYmx1ZS01MDAgdHJhbnNpdGlvbi1hbGxcIlxuICAgICAgLy8gd2hpbGVIb3Zlcj17eyBzY2FsZTogMS4xIH19XG4gICAgICAvLyB0cmFuc2l0aW9uPXt7IGR1cmF0aW9uOiAwLjUgfX1cbiAgICA+XG4gICAgICB7bGFiZWx9XG4gICAgPC9Nb3Rpb24+XG4gIClcbn1cblxuY29uc3QgTmF2aWdhdGlvbk1lbnU6IFJlYWN0LkZDPE5hdmlnYXRpb25NZW51UHJvcHM+ID0gKHsgbWVudUl0ZW1zIH0pID0+IHtcbiAgY29uc3QgW2FjdGl2ZUluZGV4LCBzZXRBY3RpdmVJbmRleF0gPSB1c2VTdGF0ZTxudW1iZXIgfCBudWxsPihudWxsKTtcblxuICBjb25zdCBoYW5kbGVNb3VzZUVudGVyID0gKGluZGV4OiBudW1iZXIpID0+IHtcbiAgICBzZXRBY3RpdmVJbmRleChpbmRleCk7XG4gIH07XG5cbiAgY29uc3QgaGFuZGxlTW91c2VMZWF2ZSA9ICgpID0+IHtcbiAgICBzZXRBY3RpdmVJbmRleChudWxsKTtcbiAgfTtcblxuICBjb25zdCByZW5kZXJNZW51SXRlbXMgPSAoaXRlbXM6IFN1Yk9wdGlvbltdKSA9PiB7XG4gICAgcmV0dXJuIChcbiAgICAgIDx1bCBzdHlsZT17e1xuICAgICAgICBmbGV4RGlyZWN0aW9uOlwicm93XCJcbiAgICAgIH19PlxuICAgICAgICB7aXRlbXMubWFwKChpdGVtLCBpbmRleCkgPT4gKFxuICAgICAgICAgIDxsaSBrZXk9e2luZGV4fSBjbGFzc05hbWU9XCJob3ZlcjpiZy1ncmF5LTcwMCByb3VuZGVkLW1kIHAtMlwiPlxuICAgICAgICAgICAge2l0ZW0ubGluayA/IChcbiAgICAgICAgICAgICAgPE5hdmlnYXRpb25NZW51TGlua1xuICAgICAgICAgICAgICAgIGxhYmVsPXtpdGVtLmxhYmVsfVxuICAgICAgICAgICAgICAgIGxpbms9e2l0ZW0ubGlua31cbiAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICk6IChcbiAgICAgICAgICAgICAgPGRpdj5cbiAgICAgICAgICAgICAgICB7aXRlbS5sYWJlbH1cbiAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICApfVxuICAgICAgICAgICAge2l0ZW0uZGVzY3JpcHRpb24gJiYgPHAgY2xhc3NOYW1lPVwidGV4dC1zbSB0ZXh0LWdyYXktNDAwXCI+e2l0ZW0uZGVzY3JpcHRpb259PC9wPn1cblxuICAgICAgICAgICAge2l0ZW0uc3ViT3B0aW9ucyAmJiAoXG4gICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwicGwtNFwiPlxuICAgICAgICAgICAgICAgIHtyZW5kZXJNZW51SXRlbXMoaXRlbS5zdWJPcHRpb25zKX1cbiAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICApfVxuICAgICAgICAgIDwvbGk+XG4gICAgICAgICkpfVxuICAgICAgPC91bD5cbiAgICApO1xuICB9O1xuXG5cblxuICByZXR1cm4gKFxuICAgIDxuYXYgY2xhc3NOYW1lPVwidy1mdWxsIGZsZXgganVzdGlmeS1jZW50ZXJcIj5cbiAgICAgIDx1bCBjbGFzc05hbWU9XCJmbGV4IGdhcC0xMlwiPlxuICAgICAgICB7bWVudUl0ZW1zLm1hcCgoaXRlbSwgaW5kZXgpID0+IChcbiAgICAgICAgICA8bGlcbiAgICAgICAgICAgIGtleT17aW5kZXh9XG4gICAgICAgICAgICBjbGFzc05hbWU9XCJyZWxhdGl2ZSBncm91cFwiXG4gICAgICAgICAgICBvbk1vdXNlRW50ZXI9eygpID0+IGhhbmRsZU1vdXNlRW50ZXIoaW5kZXgpfVxuICAgICAgICAgICAgb25Nb3VzZUxlYXZlPXtoYW5kbGVNb3VzZUxlYXZlfVxuICAgICAgICAgID5cblxuICAgICAgICAgICAgPE5hdmlnYXRpb25NZW51TGlua1xuICAgICAgICAgICAgICBsYWJlbD17aXRlbS5sYWJlbH1cbiAgICAgICAgICAgICAgbGluaz17aXRlbS5saW5rfVxuICAgICAgICAgICAgLz5cblxuICAgICAgICAgICAge2l0ZW0uc3ViT3B0aW9ucyAmJiBhY3RpdmVJbmRleCA9PT0gaW5kZXggJiYgKFxuICAgICAgICAgICAgICA8TW90aW9uXG4gICAgICAgICAgICAgICAgaW5pdGlhbD17eyBvcGFjaXR5OiAwLCB5OiAtMTAgfX1cbiAgICAgICAgICAgICAgICBhbmltYXRlPXt7IG9wYWNpdHk6IDEsIHk6IDAgfX1cbiAgICAgICAgICAgICAgICBleGl0PXt7IG9wYWNpdHk6IDAsIHk6IDEwIH19XG4gICAgICAgICAgICAgICAgdHJhbnNpdGlvbj17eyBkdXJhdGlvbjogMC4zIH19XG4gICAgICAgICAgICAgICAgLy8gY2xhc3NOYW1lPVwiYWJzb2x1dGUgdG9wLWZ1bGwgbGVmdC0wIHctZnVsbFwiXG4gICAgICAgICAgICAgID5cbiAgICAgICAgICAgICAgICB7cmVuZGVyTWVudUl0ZW1zKGl0ZW0uc3ViT3B0aW9ucyl9XG4gICAgICAgICAgICAgIDwvTW90aW9uPlxuICAgICAgICAgICAgKX1cblxuICAgICAgICAgIDwvbGk+XG4gICAgICAgICkpfVxuICAgICAgPC91bD5cbiAgICA8L25hdj5cbiAgKTtcbn07XG5cbmV4cG9ydCBkZWZhdWx0IE5hdmlnYXRpb25NZW51O1xuIl0sIm5hbWVzIjpbIlJlYWN0IiwidXNlU3RhdGUiLCJNb3Rpb24iLCJOYXZpZ2F0aW9uTWVudUxpbmsiLCJsYWJlbCIsImxpbmsiLCJ0eXBlIiwiaHJlZiIsImNsYXNzTmFtZSIsIk5hdmlnYXRpb25NZW51IiwibWVudUl0ZW1zIiwiYWN0aXZlSW5kZXgiLCJzZXRBY3RpdmVJbmRleCIsImhhbmRsZU1vdXNlRW50ZXIiLCJpbmRleCIsImhhbmRsZU1vdXNlTGVhdmUiLCJyZW5kZXJNZW51SXRlbXMiLCJpdGVtcyIsInVsIiwic3R5bGUiLCJmbGV4RGlyZWN0aW9uIiwibWFwIiwiaXRlbSIsImxpIiwiZGl2IiwiZGVzY3JpcHRpb24iLCJwIiwic3ViT3B0aW9ucyIsIm5hdiIsIm9uTW91c2VFbnRlciIsIm9uTW91c2VMZWF2ZSIsImluaXRpYWwiLCJvcGFjaXR5IiwieSIsImFuaW1hdGUiLCJleGl0IiwidHJhbnNpdGlvbiIsImR1cmF0aW9uIl0sImlnbm9yZUxpc3QiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/layouts/header/components/nav/NavigationMenu.tsx\n"));

/***/ })

});
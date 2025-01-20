"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
self["webpackHotUpdate_N_E"]("app/layout",{

/***/ "(app-pages-browser)/./src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx":
/*!******************************************************************************!*\
  !*** ./src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx ***!
  \******************************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var _components_general_buttons_ButtonBase__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/components/general/buttons/ButtonBase */ \"(app-pages-browser)/./src/components/general/buttons/ButtonBase.tsx\");\n/* harmony import */ var _components_general_dropdown_DropdownBase__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/components/general/dropdown/DropdownBase */ \"(app-pages-browser)/./src/components/general/dropdown/DropdownBase.tsx\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);\n// components/UserNavigationMenu.tsx\n/* __next_internal_client_entry_do_not_use__ default auto */ \nvar _s = $RefreshSig$();\n\n\n\nconst UserNavigationMenu = (param)=>{\n    let {} = param;\n    _s();\n    const [isLoggedIn, setIsLoggedIn] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(false);\n    const [isDropdownOpen, setIsDropdownOpen] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(false);\n    const handleLogin = ()=>{\n        setIsLoggedIn(true);\n        setIsDropdownOpen(false); // Close dropdown if it's open\n    };\n    const handleLogout = ()=>{\n        setIsLoggedIn(false);\n        setIsDropdownOpen(false); // Close dropdown on logout\n    };\n    const toggleDropdown = ()=>{\n        setIsDropdownOpen((prev)=>!prev);\n    };\n    const options = [\n        'Option 1',\n        'Option 2',\n        'Option 3',\n        'Option 4'\n    ];\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n        className: \"relative inline-block text-left\",\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n            children: !isLoggedIn ? /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                className: \"flex space-x-4\",\n                children: [\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_general_buttons_ButtonBase__WEBPACK_IMPORTED_MODULE_1__[\"default\"], {\n                        onClick: handleLogin,\n                        variant: \"primary\",\n                        children: \"LOGIN\"\n                    }, void 0, false, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 31,\n                        columnNumber: 13\n                    }, undefined),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_general_buttons_ButtonBase__WEBPACK_IMPORTED_MODULE_1__[\"default\"], {\n                        variant: \"secondary\",\n                        children: \"Sign Up\"\n                    }, void 0, false, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 34,\n                        columnNumber: 13\n                    }, undefined)\n                ]\n            }, void 0, true, {\n                fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                lineNumber: 30,\n                columnNumber: 11\n            }, undefined) : /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                children: [\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_general_buttons_ButtonBase__WEBPACK_IMPORTED_MODULE_1__[\"default\"], {\n                        onClick: toggleDropdown,\n                        className: \"flex items-center\",\n                        children: [\n                            /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"img\", {\n                                src: \"/path/to/user/icon.png\" // Replace with your user icon path\n                                ,\n                                alt: \"User Icon\",\n                                className: \"w-6 h-6 mr-2\"\n                            }, void 0, false, {\n                                fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                                lineNumber: 42,\n                                columnNumber: 15\n                            }, undefined),\n                            \"User Menu\"\n                        ]\n                    }, void 0, true, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 38,\n                        columnNumber: 13\n                    }, undefined),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_general_dropdown_DropdownBase__WEBPACK_IMPORTED_MODULE_2__[\"default\"], {\n                        options: options\n                    }, void 0, false, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 49,\n                        columnNumber: 13\n                    }, undefined)\n                ]\n            }, void 0, true, {\n                fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                lineNumber: 37,\n                columnNumber: 11\n            }, undefined)\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n            lineNumber: 28,\n            columnNumber: 7\n        }, undefined)\n    }, void 0, false, {\n        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n        lineNumber: 27,\n        columnNumber: 5\n    }, undefined);\n};\n_s(UserNavigationMenu, \"D5Fm4SpupPtlsfVq0kUeSEkqDYY=\");\n_c = UserNavigationMenu;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (UserNavigationMenu);\nvar _c;\n$RefreshReg$(_c, \"UserNavigationMenu\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9sYXlvdXRzL2hlYWRlci9nbG9iYWwtYmFyL2NvbXBvbmVudHMvdXNlci9Vc2VyTmF2aWdhdGlvbk1lbnUudHN4IiwibWFwcGluZ3MiOiI7Ozs7Ozs7OztBQUFBLG9DQUFvQzs7O0FBRTZCO0FBQ0s7QUFDOUI7QUFFeEMsTUFBTUkscUJBQStCO1FBQUMsRUFBRTs7SUFDdEMsTUFBTSxDQUFDQyxZQUFZQyxjQUFjLEdBQUdILCtDQUFRQSxDQUFDO0lBQzdDLE1BQU0sQ0FBQ0ksZ0JBQWdCQyxrQkFBa0IsR0FBR0wsK0NBQVFBLENBQUM7SUFFckQsTUFBTU0sY0FBYztRQUNsQkgsY0FBYztRQUNkRSxrQkFBa0IsUUFBUSw4QkFBOEI7SUFDMUQ7SUFFQSxNQUFNRSxlQUFlO1FBQ25CSixjQUFjO1FBQ2RFLGtCQUFrQixRQUFRLDJCQUEyQjtJQUN2RDtJQUVBLE1BQU1HLGlCQUFpQjtRQUNyQkgsa0JBQWtCLENBQUNJLE9BQVMsQ0FBQ0E7SUFDL0I7SUFDQSxNQUFNQyxVQUFVO1FBQUM7UUFBWTtRQUFZO1FBQVk7S0FBVztJQUVoRSxxQkFDRSw4REFBQ0M7UUFBSUMsV0FBVTtrQkFDYiw0RUFBQ0Q7c0JBQ0UsQ0FBQ1QsMkJBQ0EsOERBQUNTO2dCQUFJQyxXQUFVOztrQ0FDYiw4REFBQ2YsOEVBQVVBO3dCQUFDZ0IsU0FBU1A7d0JBQWFRLFNBQVE7a0NBQVU7Ozs7OztrQ0FHcEQsOERBQUNqQiw4RUFBVUE7d0JBQUNpQixTQUFRO2tDQUFZOzs7Ozs7Ozs7OzswQ0FHbEMsOERBQUNIOztrQ0FDQyw4REFBQ2QsOEVBQVVBO3dCQUNUZ0IsU0FBU0w7d0JBQ1RJLFdBQVU7OzBDQUVWLDhEQUFDRztnQ0FDQ0MsS0FBSSx5QkFBeUIsbUNBQW1DOztnQ0FDaEVDLEtBQUk7Z0NBQ0pMLFdBQVU7Ozs7Ozs0QkFDVjs7Ozs7OztrQ0FHSiw4REFBQ2QsaUZBQVlBO3dCQUNUWSxTQUFTQTs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQVN6QjtHQXBETVQ7S0FBQUE7QUFzRE4saUVBQWVBLGtCQUFrQkEsRUFBQyIsInNvdXJjZXMiOlsiL2NvZGUvc3JjL2xheW91dHMvaGVhZGVyL2dsb2JhbC1iYXIvY29tcG9uZW50cy91c2VyL1VzZXJOYXZpZ2F0aW9uTWVudS50c3giXSwic291cmNlc0NvbnRlbnQiOlsiLy8gY29tcG9uZW50cy9Vc2VyTmF2aWdhdGlvbk1lbnUudHN4XG5cInVzZSBjbGllbnRcIlxuaW1wb3J0IEJ1dHRvbkJhc2UgZnJvbSAnQC9jb21wb25lbnRzL2dlbmVyYWwvYnV0dG9ucy9CdXR0b25CYXNlJztcbmltcG9ydCBEcm9wZG93bkJhc2UgZnJvbSAnQC9jb21wb25lbnRzL2dlbmVyYWwvZHJvcGRvd24vRHJvcGRvd25CYXNlJztcbmltcG9ydCBSZWFjdCwgeyB1c2VTdGF0ZSB9IGZyb20gJ3JlYWN0JztcblxuY29uc3QgVXNlck5hdmlnYXRpb25NZW51OiBSZWFjdC5GQyA9ICh7fSkgPT4ge1xuICBjb25zdCBbaXNMb2dnZWRJbiwgc2V0SXNMb2dnZWRJbl0gPSB1c2VTdGF0ZShmYWxzZSk7XG4gIGNvbnN0IFtpc0Ryb3Bkb3duT3Blbiwgc2V0SXNEcm9wZG93bk9wZW5dID0gdXNlU3RhdGUoZmFsc2UpO1xuXG4gIGNvbnN0IGhhbmRsZUxvZ2luID0gKCkgPT4ge1xuICAgIHNldElzTG9nZ2VkSW4odHJ1ZSk7XG4gICAgc2V0SXNEcm9wZG93bk9wZW4oZmFsc2UpOyAvLyBDbG9zZSBkcm9wZG93biBpZiBpdCdzIG9wZW5cbiAgfTtcblxuICBjb25zdCBoYW5kbGVMb2dvdXQgPSAoKSA9PiB7XG4gICAgc2V0SXNMb2dnZWRJbihmYWxzZSk7XG4gICAgc2V0SXNEcm9wZG93bk9wZW4oZmFsc2UpOyAvLyBDbG9zZSBkcm9wZG93biBvbiBsb2dvdXRcbiAgfTtcblxuICBjb25zdCB0b2dnbGVEcm9wZG93biA9ICgpID0+IHtcbiAgICBzZXRJc0Ryb3Bkb3duT3BlbigocHJldikgPT4gIXByZXYpO1xuICB9O1xuICBjb25zdCBvcHRpb25zID0gWydPcHRpb24gMScsICdPcHRpb24gMicsICdPcHRpb24gMycsICdPcHRpb24gNCddO1xuXG4gIHJldHVybiAoXG4gICAgPGRpdiBjbGFzc05hbWU9XCJyZWxhdGl2ZSBpbmxpbmUtYmxvY2sgdGV4dC1sZWZ0XCI+XG4gICAgICA8ZGl2PlxuICAgICAgICB7IWlzTG9nZ2VkSW4gPyAoXG4gICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJmbGV4IHNwYWNlLXgtNFwiPlxuICAgICAgICAgICAgPEJ1dHRvbkJhc2Ugb25DbGljaz17aGFuZGxlTG9naW59IHZhcmlhbnQ9XCJwcmltYXJ5XCI+XG4gICAgICAgICAgICAgIExPR0lOXG4gICAgICAgICAgICA8L0J1dHRvbkJhc2U+XG4gICAgICAgICAgICA8QnV0dG9uQmFzZSB2YXJpYW50PVwic2Vjb25kYXJ5XCI+U2lnbiBVcDwvQnV0dG9uQmFzZT5cbiAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgKSA6IChcbiAgICAgICAgICA8ZGl2PlxuICAgICAgICAgICAgPEJ1dHRvbkJhc2VcbiAgICAgICAgICAgICAgb25DbGljaz17dG9nZ2xlRHJvcGRvd259XG4gICAgICAgICAgICAgIGNsYXNzTmFtZT1cImZsZXggaXRlbXMtY2VudGVyXCJcbiAgICAgICAgICAgID5cbiAgICAgICAgICAgICAgPGltZ1xuICAgICAgICAgICAgICAgIHNyYz1cIi9wYXRoL3RvL3VzZXIvaWNvbi5wbmdcIiAvLyBSZXBsYWNlIHdpdGggeW91ciB1c2VyIGljb24gcGF0aFxuICAgICAgICAgICAgICAgIGFsdD1cIlVzZXIgSWNvblwiXG4gICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwidy02IGgtNiBtci0yXCJcbiAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgVXNlciBNZW51XG4gICAgICAgICAgICA8L0J1dHRvbkJhc2U+XG4gICAgICAgICAgICA8RHJvcGRvd25CYXNlXG4gICAgICAgICAgICAgICAgb3B0aW9ucz17b3B0aW9uc31cbiAgICAgICAgICAgICAgICAvLyBmb2xsb3dNb3VzZT17dHJ1ZX1cbiAgICAgICAgICAgIC8+XG5cbiAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgKX1cbiAgICAgIDwvZGl2PlxuICAgIDwvZGl2PlxuICApO1xufTtcblxuZXhwb3J0IGRlZmF1bHQgVXNlck5hdmlnYXRpb25NZW51O1xuIl0sIm5hbWVzIjpbIkJ1dHRvbkJhc2UiLCJEcm9wZG93bkJhc2UiLCJSZWFjdCIsInVzZVN0YXRlIiwiVXNlck5hdmlnYXRpb25NZW51IiwiaXNMb2dnZWRJbiIsInNldElzTG9nZ2VkSW4iLCJpc0Ryb3Bkb3duT3BlbiIsInNldElzRHJvcGRvd25PcGVuIiwiaGFuZGxlTG9naW4iLCJoYW5kbGVMb2dvdXQiLCJ0b2dnbGVEcm9wZG93biIsInByZXYiLCJvcHRpb25zIiwiZGl2IiwiY2xhc3NOYW1lIiwib25DbGljayIsInZhcmlhbnQiLCJpbWciLCJzcmMiLCJhbHQiXSwiaWdub3JlTGlzdCI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\n"));

/***/ })

});
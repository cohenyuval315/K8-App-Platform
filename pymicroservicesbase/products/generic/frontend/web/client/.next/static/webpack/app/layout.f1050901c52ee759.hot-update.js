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

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var _components_general_buttons_ButtonBase__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/components/general/buttons/ButtonBase */ \"(app-pages-browser)/./src/components/general/buttons/ButtonBase.tsx\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);\n// components/UserNavigationMenu.tsx\n/* __next_internal_client_entry_do_not_use__ default auto */ \nvar _s = $RefreshSig$();\n\n\nconst UserNavigationMenu = (param)=>{\n    let {} = param;\n    _s();\n    const [isLoggedIn, setIsLoggedIn] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(false);\n    const [isDropdownOpen, setIsDropdownOpen] = (0,react__WEBPACK_IMPORTED_MODULE_2__.useState)(false);\n    const handleLogin = ()=>{\n        setIsLoggedIn(true);\n        setIsDropdownOpen(false); // Close dropdown if it's open\n    };\n    const handleLogout = ()=>{\n        setIsLoggedIn(false);\n        setIsDropdownOpen(false); // Close dropdown on logout\n    };\n    const toggleDropdown = ()=>{\n        setIsDropdownOpen((prev)=>!prev);\n    };\n    const options = [\n        'Option 1',\n        'Option 2',\n        'Option 3',\n        'Option 4'\n    ];\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n        className: \"relative inline-block text-left\",\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n            children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n                className: \"flex space-x-4\",\n                children: [\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_general_buttons_ButtonBase__WEBPACK_IMPORTED_MODULE_1__[\"default\"], {\n                        onClick: handleLogin,\n                        variant: \"primary\",\n                        children: \"LOGIN\"\n                    }, void 0, false, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 30,\n                        columnNumber: 11\n                    }, undefined),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"button\", {\n                        children: \"LOGIN\"\n                    }, void 0, false, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 33,\n                        columnNumber: 11\n                    }, undefined),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"button\", {\n                        children: \"SIGNUP\"\n                    }, void 0, false, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 36,\n                        columnNumber: 11\n                    }, undefined),\n                    /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_general_buttons_ButtonBase__WEBPACK_IMPORTED_MODULE_1__[\"default\"], {\n                        variant: \"secondary\",\n                        children: \"Sign Up\"\n                    }, void 0, false, {\n                        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                        lineNumber: 39,\n                        columnNumber: 11\n                    }, undefined)\n                ]\n            }, void 0, true, {\n                fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n                lineNumber: 29,\n                columnNumber: 9\n            }, undefined)\n        }, void 0, false, {\n            fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n            lineNumber: 28,\n            columnNumber: 7\n        }, undefined)\n    }, void 0, false, {\n        fileName: \"/code/src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\",\n        lineNumber: 27,\n        columnNumber: 5\n    }, undefined);\n};\n_s(UserNavigationMenu, \"D5Fm4SpupPtlsfVq0kUeSEkqDYY=\");\n_c = UserNavigationMenu;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (UserNavigationMenu);\nvar _c;\n$RefreshReg$(_c, \"UserNavigationMenu\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9sYXlvdXRzL2hlYWRlci9nbG9iYWwtYmFyL2NvbXBvbmVudHMvdXNlci9Vc2VyTmF2aWdhdGlvbk1lbnUudHN4IiwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUEsb0NBQW9DOzs7QUFFNkI7QUFFekI7QUFFeEMsTUFBTUcscUJBQStCO1FBQUMsRUFBRTs7SUFDdEMsTUFBTSxDQUFDQyxZQUFZQyxjQUFjLEdBQUdILCtDQUFRQSxDQUFDO0lBQzdDLE1BQU0sQ0FBQ0ksZ0JBQWdCQyxrQkFBa0IsR0FBR0wsK0NBQVFBLENBQUM7SUFFckQsTUFBTU0sY0FBYztRQUNsQkgsY0FBYztRQUNkRSxrQkFBa0IsUUFBUSw4QkFBOEI7SUFDMUQ7SUFFQSxNQUFNRSxlQUFlO1FBQ25CSixjQUFjO1FBQ2RFLGtCQUFrQixRQUFRLDJCQUEyQjtJQUN2RDtJQUVBLE1BQU1HLGlCQUFpQjtRQUNyQkgsa0JBQWtCLENBQUNJLE9BQVMsQ0FBQ0E7SUFDL0I7SUFDQSxNQUFNQyxVQUFVO1FBQUM7UUFBWTtRQUFZO1FBQVk7S0FBVztJQUVoRSxxQkFDRSw4REFBQ0M7UUFBSUMsV0FBVTtrQkFDYiw0RUFBQ0Q7c0JBQ0MsNEVBQUNBO2dCQUFJQyxXQUFVOztrQ0FDYiw4REFBQ2QsOEVBQVVBO3dCQUFDZSxTQUFTUDt3QkFBYVEsU0FBUTtrQ0FBVTs7Ozs7O2tDQUdwRCw4REFBQ0M7a0NBQU87Ozs7OztrQ0FHUiw4REFBQ0E7a0NBQU87Ozs7OztrQ0FHUiw4REFBQ2pCLDhFQUFVQTt3QkFBQ2dCLFNBQVE7a0NBQVk7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFLMUM7R0FyQ01iO0tBQUFBO0FBdUNOLGlFQUFlQSxrQkFBa0JBLEVBQUMiLCJzb3VyY2VzIjpbIi9jb2RlL3NyYy9sYXlvdXRzL2hlYWRlci9nbG9iYWwtYmFyL2NvbXBvbmVudHMvdXNlci9Vc2VyTmF2aWdhdGlvbk1lbnUudHN4Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIGNvbXBvbmVudHMvVXNlck5hdmlnYXRpb25NZW51LnRzeFxuXCJ1c2UgY2xpZW50XCJcbmltcG9ydCBCdXR0b25CYXNlIGZyb20gJ0AvY29tcG9uZW50cy9nZW5lcmFsL2J1dHRvbnMvQnV0dG9uQmFzZSc7XG5pbXBvcnQgRHJvcGRvd25CYXNlIGZyb20gJ0AvY29tcG9uZW50cy9nZW5lcmFsL2Ryb3Bkb3duL0Ryb3Bkb3duQmFzZSc7XG5pbXBvcnQgUmVhY3QsIHsgdXNlU3RhdGUgfSBmcm9tICdyZWFjdCc7XG5cbmNvbnN0IFVzZXJOYXZpZ2F0aW9uTWVudTogUmVhY3QuRkMgPSAoe30pID0+IHtcbiAgY29uc3QgW2lzTG9nZ2VkSW4sIHNldElzTG9nZ2VkSW5dID0gdXNlU3RhdGUoZmFsc2UpO1xuICBjb25zdCBbaXNEcm9wZG93bk9wZW4sIHNldElzRHJvcGRvd25PcGVuXSA9IHVzZVN0YXRlKGZhbHNlKTtcblxuICBjb25zdCBoYW5kbGVMb2dpbiA9ICgpID0+IHtcbiAgICBzZXRJc0xvZ2dlZEluKHRydWUpO1xuICAgIHNldElzRHJvcGRvd25PcGVuKGZhbHNlKTsgLy8gQ2xvc2UgZHJvcGRvd24gaWYgaXQncyBvcGVuXG4gIH07XG5cbiAgY29uc3QgaGFuZGxlTG9nb3V0ID0gKCkgPT4ge1xuICAgIHNldElzTG9nZ2VkSW4oZmFsc2UpO1xuICAgIHNldElzRHJvcGRvd25PcGVuKGZhbHNlKTsgLy8gQ2xvc2UgZHJvcGRvd24gb24gbG9nb3V0XG4gIH07XG5cbiAgY29uc3QgdG9nZ2xlRHJvcGRvd24gPSAoKSA9PiB7XG4gICAgc2V0SXNEcm9wZG93bk9wZW4oKHByZXYpID0+ICFwcmV2KTtcbiAgfTtcbiAgY29uc3Qgb3B0aW9ucyA9IFsnT3B0aW9uIDEnLCAnT3B0aW9uIDInLCAnT3B0aW9uIDMnLCAnT3B0aW9uIDQnXTtcblxuICByZXR1cm4gKFxuICAgIDxkaXYgY2xhc3NOYW1lPVwicmVsYXRpdmUgaW5saW5lLWJsb2NrIHRleHQtbGVmdFwiPlxuICAgICAgPGRpdj5cbiAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJmbGV4IHNwYWNlLXgtNFwiPlxuICAgICAgICAgIDxCdXR0b25CYXNlIG9uQ2xpY2s9e2hhbmRsZUxvZ2lufSB2YXJpYW50PVwicHJpbWFyeVwiPlxuICAgICAgICAgICAgTE9HSU5cbiAgICAgICAgICA8L0J1dHRvbkJhc2U+XG4gICAgICAgICAgPGJ1dHRvbj5cbiAgICAgICAgICAgIExPR0lOXG4gICAgICAgICAgPC9idXR0b24+XG4gICAgICAgICAgPGJ1dHRvbj5cbiAgICAgICAgICAgIFNJR05VUFxuICAgICAgICAgIDwvYnV0dG9uPlxuICAgICAgICAgIDxCdXR0b25CYXNlIHZhcmlhbnQ9XCJzZWNvbmRhcnlcIj5TaWduIFVwPC9CdXR0b25CYXNlPlxuICAgICAgICA8L2Rpdj5cbiAgICAgIDwvZGl2PlxuICAgIDwvZGl2PlxuICApO1xufTtcblxuZXhwb3J0IGRlZmF1bHQgVXNlck5hdmlnYXRpb25NZW51O1xuIl0sIm5hbWVzIjpbIkJ1dHRvbkJhc2UiLCJSZWFjdCIsInVzZVN0YXRlIiwiVXNlck5hdmlnYXRpb25NZW51IiwiaXNMb2dnZWRJbiIsInNldElzTG9nZ2VkSW4iLCJpc0Ryb3Bkb3duT3BlbiIsInNldElzRHJvcGRvd25PcGVuIiwiaGFuZGxlTG9naW4iLCJoYW5kbGVMb2dvdXQiLCJ0b2dnbGVEcm9wZG93biIsInByZXYiLCJvcHRpb25zIiwiZGl2IiwiY2xhc3NOYW1lIiwib25DbGljayIsInZhcmlhbnQiLCJidXR0b24iXSwiaWdub3JlTGlzdCI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/layouts/header/global-bar/components/user/UserNavigationMenu.tsx\n"));

/***/ })

});
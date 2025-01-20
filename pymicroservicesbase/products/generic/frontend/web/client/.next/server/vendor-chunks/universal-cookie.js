"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
exports.id = "vendor-chunks/universal-cookie";
exports.ids = ["vendor-chunks/universal-cookie"];
exports.modules = {

/***/ "(ssr)/./node_modules/universal-cookie/esm/index.mjs":
/*!*****************************************************!*\
  !*** ./node_modules/universal-cookie/esm/index.mjs ***!
  \*****************************************************/
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ Cookies)\n/* harmony export */ });\nvar cookie = {};\n\n/*!\n * cookie\n * Copyright(c) 2012-2014 Roman Shtylman\n * Copyright(c) 2015 Douglas Christopher Wilson\n * MIT Licensed\n */\n\nvar hasRequiredCookie;\n\nfunction requireCookie () {\n\tif (hasRequiredCookie) return cookie;\n\thasRequiredCookie = 1;\n\n\t/**\n\t * Module exports.\n\t * @public\n\t */\n\n\tcookie.parse = parse;\n\tcookie.serialize = serialize;\n\n\t/**\n\t * Module variables.\n\t * @private\n\t */\n\n\tvar __toString = Object.prototype.toString;\n\tvar __hasOwnProperty = Object.prototype.hasOwnProperty;\n\n\t/**\n\t * RegExp to match cookie-name in RFC 6265 sec 4.1.1\n\t * This refers out to the obsoleted definition of token in RFC 2616 sec 2.2\n\t * which has been replaced by the token definition in RFC 7230 appendix B.\n\t *\n\t * cookie-name       = token\n\t * token             = 1*tchar\n\t * tchar             = \"!\" / \"#\" / \"$\" / \"%\" / \"&\" / \"'\" /\n\t *                     \"*\" / \"+\" / \"-\" / \".\" / \"^\" / \"_\" /\n\t *                     \"`\" / \"|\" / \"~\" / DIGIT / ALPHA\n\t */\n\n\tvar cookieNameRegExp = /^[!#$%&'*+\\-.^_`|~0-9A-Za-z]+$/;\n\n\t/**\n\t * RegExp to match cookie-value in RFC 6265 sec 4.1.1\n\t *\n\t * cookie-value      = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE )\n\t * cookie-octet      = %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E\n\t *                     ; US-ASCII characters excluding CTLs,\n\t *                     ; whitespace DQUOTE, comma, semicolon,\n\t *                     ; and backslash\n\t */\n\n\tvar cookieValueRegExp = /^(\"?)[\\u0021\\u0023-\\u002B\\u002D-\\u003A\\u003C-\\u005B\\u005D-\\u007E]*\\1$/;\n\n\t/**\n\t * RegExp to match domain-value in RFC 6265 sec 4.1.1\n\t *\n\t * domain-value      = <subdomain>\n\t *                     ; defined in [RFC1034], Section 3.5, as\n\t *                     ; enhanced by [RFC1123], Section 2.1\n\t * <subdomain>       = <label> | <subdomain> \".\" <label>\n\t * <label>           = <let-dig> [ [ <ldh-str> ] <let-dig> ]\n\t *                     Labels must be 63 characters or less.\n\t *                     'let-dig' not 'letter' in the first char, per RFC1123\n\t * <ldh-str>         = <let-dig-hyp> | <let-dig-hyp> <ldh-str>\n\t * <let-dig-hyp>     = <let-dig> | \"-\"\n\t * <let-dig>         = <letter> | <digit>\n\t * <letter>          = any one of the 52 alphabetic characters A through Z in\n\t *                     upper case and a through z in lower case\n\t * <digit>           = any one of the ten digits 0 through 9\n\t *\n\t * Keep support for leading dot: https://github.com/jshttp/cookie/issues/173\n\t *\n\t * > (Note that a leading %x2E (\".\"), if present, is ignored even though that\n\t * character is not permitted, but a trailing %x2E (\".\"), if present, will\n\t * cause the user agent to ignore the attribute.)\n\t */\n\n\tvar domainValueRegExp = /^([.]?[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?)([.][a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?)*$/i;\n\n\t/**\n\t * RegExp to match path-value in RFC 6265 sec 4.1.1\n\t *\n\t * path-value        = <any CHAR except CTLs or \";\">\n\t * CHAR              = %x01-7F\n\t *                     ; defined in RFC 5234 appendix B.1\n\t */\n\n\tvar pathValueRegExp = /^[\\u0020-\\u003A\\u003D-\\u007E]*$/;\n\n\t/**\n\t * Parse a cookie header.\n\t *\n\t * Parse the given cookie header string into an object\n\t * The object has the various cookies as keys(names) => values\n\t *\n\t * @param {string} str\n\t * @param {object} [opt]\n\t * @return {object}\n\t * @public\n\t */\n\n\tfunction parse(str, opt) {\n\t  if (typeof str !== 'string') {\n\t    throw new TypeError('argument str must be a string');\n\t  }\n\n\t  var obj = {};\n\t  var len = str.length;\n\t  // RFC 6265 sec 4.1.1, RFC 2616 2.2 defines a cookie name consists of one char minimum, plus '='.\n\t  if (len < 2) return obj;\n\n\t  var dec = (opt && opt.decode) || decode;\n\t  var index = 0;\n\t  var eqIdx = 0;\n\t  var endIdx = 0;\n\n\t  do {\n\t    eqIdx = str.indexOf('=', index);\n\t    if (eqIdx === -1) break; // No more cookie pairs.\n\n\t    endIdx = str.indexOf(';', index);\n\n\t    if (endIdx === -1) {\n\t      endIdx = len;\n\t    } else if (eqIdx > endIdx) {\n\t      // backtrack on prior semicolon\n\t      index = str.lastIndexOf(';', eqIdx - 1) + 1;\n\t      continue;\n\t    }\n\n\t    var keyStartIdx = startIndex(str, index, eqIdx);\n\t    var keyEndIdx = endIndex(str, eqIdx, keyStartIdx);\n\t    var key = str.slice(keyStartIdx, keyEndIdx);\n\n\t    // only assign once\n\t    if (!__hasOwnProperty.call(obj, key)) {\n\t      var valStartIdx = startIndex(str, eqIdx + 1, endIdx);\n\t      var valEndIdx = endIndex(str, endIdx, valStartIdx);\n\n\t      if (str.charCodeAt(valStartIdx) === 0x22 /* \" */ && str.charCodeAt(valEndIdx - 1) === 0x22 /* \" */) {\n\t        valStartIdx++;\n\t        valEndIdx--;\n\t      }\n\n\t      var val = str.slice(valStartIdx, valEndIdx);\n\t      obj[key] = tryDecode(val, dec);\n\t    }\n\n\t    index = endIdx + 1;\n\t  } while (index < len);\n\n\t  return obj;\n\t}\n\n\tfunction startIndex(str, index, max) {\n\t  do {\n\t    var code = str.charCodeAt(index);\n\t    if (code !== 0x20 /*   */ && code !== 0x09 /* \\t */) return index;\n\t  } while (++index < max);\n\t  return max;\n\t}\n\n\tfunction endIndex(str, index, min) {\n\t  while (index > min) {\n\t    var code = str.charCodeAt(--index);\n\t    if (code !== 0x20 /*   */ && code !== 0x09 /* \\t */) return index + 1;\n\t  }\n\t  return min;\n\t}\n\n\t/**\n\t * Serialize data into a cookie header.\n\t *\n\t * Serialize a name value pair into a cookie string suitable for\n\t * http headers. An optional options object specifies cookie parameters.\n\t *\n\t * serialize('foo', 'bar', { httpOnly: true })\n\t *   => \"foo=bar; httpOnly\"\n\t *\n\t * @param {string} name\n\t * @param {string} val\n\t * @param {object} [opt]\n\t * @return {string}\n\t * @public\n\t */\n\n\tfunction serialize(name, val, opt) {\n\t  var enc = (opt && opt.encode) || encodeURIComponent;\n\n\t  if (typeof enc !== 'function') {\n\t    throw new TypeError('option encode is invalid');\n\t  }\n\n\t  if (!cookieNameRegExp.test(name)) {\n\t    throw new TypeError('argument name is invalid');\n\t  }\n\n\t  var value = enc(val);\n\n\t  if (!cookieValueRegExp.test(value)) {\n\t    throw new TypeError('argument val is invalid');\n\t  }\n\n\t  var str = name + '=' + value;\n\t  if (!opt) return str;\n\n\t  if (null != opt.maxAge) {\n\t    var maxAge = Math.floor(opt.maxAge);\n\n\t    if (!isFinite(maxAge)) {\n\t      throw new TypeError('option maxAge is invalid')\n\t    }\n\n\t    str += '; Max-Age=' + maxAge;\n\t  }\n\n\t  if (opt.domain) {\n\t    if (!domainValueRegExp.test(opt.domain)) {\n\t      throw new TypeError('option domain is invalid');\n\t    }\n\n\t    str += '; Domain=' + opt.domain;\n\t  }\n\n\t  if (opt.path) {\n\t    if (!pathValueRegExp.test(opt.path)) {\n\t      throw new TypeError('option path is invalid');\n\t    }\n\n\t    str += '; Path=' + opt.path;\n\t  }\n\n\t  if (opt.expires) {\n\t    var expires = opt.expires;\n\n\t    if (!isDate(expires) || isNaN(expires.valueOf())) {\n\t      throw new TypeError('option expires is invalid');\n\t    }\n\n\t    str += '; Expires=' + expires.toUTCString();\n\t  }\n\n\t  if (opt.httpOnly) {\n\t    str += '; HttpOnly';\n\t  }\n\n\t  if (opt.secure) {\n\t    str += '; Secure';\n\t  }\n\n\t  if (opt.partitioned) {\n\t    str += '; Partitioned';\n\t  }\n\n\t  if (opt.priority) {\n\t    var priority = typeof opt.priority === 'string'\n\t      ? opt.priority.toLowerCase() : opt.priority;\n\n\t    switch (priority) {\n\t      case 'low':\n\t        str += '; Priority=Low';\n\t        break\n\t      case 'medium':\n\t        str += '; Priority=Medium';\n\t        break\n\t      case 'high':\n\t        str += '; Priority=High';\n\t        break\n\t      default:\n\t        throw new TypeError('option priority is invalid')\n\t    }\n\t  }\n\n\t  if (opt.sameSite) {\n\t    var sameSite = typeof opt.sameSite === 'string'\n\t      ? opt.sameSite.toLowerCase() : opt.sameSite;\n\n\t    switch (sameSite) {\n\t      case true:\n\t        str += '; SameSite=Strict';\n\t        break;\n\t      case 'lax':\n\t        str += '; SameSite=Lax';\n\t        break;\n\t      case 'strict':\n\t        str += '; SameSite=Strict';\n\t        break;\n\t      case 'none':\n\t        str += '; SameSite=None';\n\t        break;\n\t      default:\n\t        throw new TypeError('option sameSite is invalid');\n\t    }\n\t  }\n\n\t  return str;\n\t}\n\n\t/**\n\t * URL-decode string value. Optimized to skip native call when no %.\n\t *\n\t * @param {string} str\n\t * @returns {string}\n\t */\n\n\tfunction decode (str) {\n\t  return str.indexOf('%') !== -1\n\t    ? decodeURIComponent(str)\n\t    : str\n\t}\n\n\t/**\n\t * Determine if value is a Date.\n\t *\n\t * @param {*} val\n\t * @private\n\t */\n\n\tfunction isDate (val) {\n\t  return __toString.call(val) === '[object Date]';\n\t}\n\n\t/**\n\t * Try decoding a string using a decoding function.\n\t *\n\t * @param {string} str\n\t * @param {function} decode\n\t * @private\n\t */\n\n\tfunction tryDecode(str, decode) {\n\t  try {\n\t    return decode(str);\n\t  } catch (e) {\n\t    return str;\n\t  }\n\t}\n\treturn cookie;\n}\n\nvar cookieExports = requireCookie();\n\nfunction hasDocumentCookie() {\n    const testingValue = typeof global === 'undefined'\n        ? undefined\n        : global.TEST_HAS_DOCUMENT_COOKIE;\n    if (typeof testingValue === 'boolean') {\n        return testingValue;\n    }\n    // Can we get/set cookies on document.cookie?\n    return typeof document === 'object' && typeof document.cookie === 'string';\n}\nfunction parseCookies(cookies) {\n    if (typeof cookies === 'string') {\n        return cookieExports.parse(cookies);\n    }\n    else if (typeof cookies === 'object' && cookies !== null) {\n        return cookies;\n    }\n    else {\n        return {};\n    }\n}\nfunction readCookie(value, options = {}) {\n    const cleanValue = cleanupCookieValue(value);\n    if (!options.doNotParse) {\n        try {\n            return JSON.parse(cleanValue);\n        }\n        catch (e) {\n            // At least we tried\n        }\n    }\n    // Ignore clean value if we failed the deserialization\n    // It is not relevant anymore to trim those values\n    return value;\n}\nfunction cleanupCookieValue(value) {\n    // express prepend j: before serializing a cookie\n    if (value && value[0] === 'j' && value[1] === ':') {\n        return value.substr(2);\n    }\n    return value;\n}\n\nclass Cookies {\n    constructor(cookies, defaultSetOptions = {}) {\n        this.changeListeners = [];\n        this.HAS_DOCUMENT_COOKIE = false;\n        this.update = () => {\n            if (!this.HAS_DOCUMENT_COOKIE) {\n                return;\n            }\n            const previousCookies = this.cookies;\n            this.cookies = cookieExports.parse(document.cookie);\n            this._checkChanges(previousCookies);\n        };\n        const domCookies = typeof document === 'undefined' ? '' : document.cookie;\n        this.cookies = parseCookies(cookies || domCookies);\n        this.defaultSetOptions = defaultSetOptions;\n        this.HAS_DOCUMENT_COOKIE = hasDocumentCookie();\n    }\n    _emitChange(params) {\n        for (let i = 0; i < this.changeListeners.length; ++i) {\n            this.changeListeners[i](params);\n        }\n    }\n    _checkChanges(previousCookies) {\n        const names = new Set(Object.keys(previousCookies).concat(Object.keys(this.cookies)));\n        names.forEach((name) => {\n            if (previousCookies[name] !== this.cookies[name]) {\n                this._emitChange({\n                    name,\n                    value: readCookie(this.cookies[name]),\n                });\n            }\n        });\n    }\n    _startPolling() {\n        this.pollingInterval = setInterval(this.update, 300);\n    }\n    _stopPolling() {\n        if (this.pollingInterval) {\n            clearInterval(this.pollingInterval);\n        }\n    }\n    get(name, options = {}) {\n        if (!options.doNotUpdate) {\n            this.update();\n        }\n        return readCookie(this.cookies[name], options);\n    }\n    getAll(options = {}) {\n        if (!options.doNotUpdate) {\n            this.update();\n        }\n        const result = {};\n        for (let name in this.cookies) {\n            result[name] = readCookie(this.cookies[name], options);\n        }\n        return result;\n    }\n    set(name, value, options) {\n        if (options) {\n            options = Object.assign(Object.assign({}, this.defaultSetOptions), options);\n        }\n        else {\n            options = this.defaultSetOptions;\n        }\n        const stringValue = typeof value === 'string' ? value : JSON.stringify(value);\n        this.cookies = Object.assign(Object.assign({}, this.cookies), { [name]: stringValue });\n        if (this.HAS_DOCUMENT_COOKIE) {\n            document.cookie = cookieExports.serialize(name, stringValue, options);\n        }\n        this._emitChange({ name, value, options });\n    }\n    remove(name, options) {\n        const finalOptions = (options = Object.assign(Object.assign(Object.assign({}, this.defaultSetOptions), options), { expires: new Date(1970, 1, 1, 0, 0, 1), maxAge: 0 }));\n        this.cookies = Object.assign({}, this.cookies);\n        delete this.cookies[name];\n        if (this.HAS_DOCUMENT_COOKIE) {\n            document.cookie = cookieExports.serialize(name, '', finalOptions);\n        }\n        this._emitChange({ name, value: undefined, options });\n    }\n    addChangeListener(callback) {\n        this.changeListeners.push(callback);\n        if (this.HAS_DOCUMENT_COOKIE && this.changeListeners.length === 1) {\n            if (typeof window === 'object' && 'cookieStore' in window) {\n                window.cookieStore.addEventListener('change', this.update);\n            }\n            else {\n                this._startPolling();\n            }\n        }\n    }\n    removeChangeListener(callback) {\n        const idx = this.changeListeners.indexOf(callback);\n        if (idx >= 0) {\n            this.changeListeners.splice(idx, 1);\n        }\n        if (this.HAS_DOCUMENT_COOKIE && this.changeListeners.length === 0) {\n            if (typeof window === 'object' && 'cookieStore' in window) {\n                window.cookieStore.removeEventListener('change', this.update);\n            }\n            else {\n                this._stopPolling();\n            }\n        }\n    }\n}\n\n\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHNzcikvLi9ub2RlX21vZHVsZXMvdW5pdmVyc2FsLWNvb2tpZS9lc20vaW5kZXgubWpzIiwibWFwcGluZ3MiOiI7Ozs7QUFBQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSwwQkFBMEI7QUFDMUIsMEJBQTBCO0FBQzFCLDBCQUEwQjtBQUMxQjs7QUFFQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLDBCQUEwQjtBQUMxQiwwQkFBMEI7QUFDMUI7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQSxtREFBbUQsS0FBSyxrQ0FBa0MsS0FBSzs7QUFFL0Y7QUFDQTtBQUNBO0FBQ0EsbURBQW1EO0FBQ25EO0FBQ0EsMEJBQTBCO0FBQzFCOztBQUVBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFlBQVksUUFBUTtBQUNwQixZQUFZLFFBQVE7QUFDcEIsYUFBYTtBQUNiO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBLDhCQUE4Qjs7QUFFOUIsNEJBQTRCOztBQUU1QjtBQUNBO0FBQ0EsT0FBTztBQUNQO0FBQ0EsaUNBQWlDO0FBQ2pDO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBLEtBQUs7O0FBRUw7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O0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRThCIiwic291cmNlcyI6WyIvY29kZS9ub2RlX21vZHVsZXMvdW5pdmVyc2FsLWNvb2tpZS9lc20vaW5kZXgubWpzIl0sInNvdXJjZXNDb250ZW50IjpbInZhciBjb29raWUgPSB7fTtcblxuLyohXG4gKiBjb29raWVcbiAqIENvcHlyaWdodChjKSAyMDEyLTIwMTQgUm9tYW4gU2h0eWxtYW5cbiAqIENvcHlyaWdodChjKSAyMDE1IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uXG4gKiBNSVQgTGljZW5zZWRcbiAqL1xuXG52YXIgaGFzUmVxdWlyZWRDb29raWU7XG5cbmZ1bmN0aW9uIHJlcXVpcmVDb29raWUgKCkge1xuXHRpZiAoaGFzUmVxdWlyZWRDb29raWUpIHJldHVybiBjb29raWU7XG5cdGhhc1JlcXVpcmVkQ29va2llID0gMTtcblxuXHQvKipcblx0ICogTW9kdWxlIGV4cG9ydHMuXG5cdCAqIEBwdWJsaWNcblx0ICovXG5cblx0Y29va2llLnBhcnNlID0gcGFyc2U7XG5cdGNvb2tpZS5zZXJpYWxpemUgPSBzZXJpYWxpemU7XG5cblx0LyoqXG5cdCAqIE1vZHVsZSB2YXJpYWJsZXMuXG5cdCAqIEBwcml2YXRlXG5cdCAqL1xuXG5cdHZhciBfX3RvU3RyaW5nID0gT2JqZWN0LnByb3RvdHlwZS50b1N0cmluZztcblx0dmFyIF9faGFzT3duUHJvcGVydHkgPSBPYmplY3QucHJvdG90eXBlLmhhc093blByb3BlcnR5O1xuXG5cdC8qKlxuXHQgKiBSZWdFeHAgdG8gbWF0Y2ggY29va2llLW5hbWUgaW4gUkZDIDYyNjUgc2VjIDQuMS4xXG5cdCAqIFRoaXMgcmVmZXJzIG91dCB0byB0aGUgb2Jzb2xldGVkIGRlZmluaXRpb24gb2YgdG9rZW4gaW4gUkZDIDI2MTYgc2VjIDIuMlxuXHQgKiB3aGljaCBoYXMgYmVlbiByZXBsYWNlZCBieSB0aGUgdG9rZW4gZGVmaW5pdGlvbiBpbiBSRkMgNzIzMCBhcHBlbmRpeCBCLlxuXHQgKlxuXHQgKiBjb29raWUtbmFtZSAgICAgICA9IHRva2VuXG5cdCAqIHRva2VuICAgICAgICAgICAgID0gMSp0Y2hhclxuXHQgKiB0Y2hhciAgICAgICAgICAgICA9IFwiIVwiIC8gXCIjXCIgLyBcIiRcIiAvIFwiJVwiIC8gXCImXCIgLyBcIidcIiAvXG5cdCAqICAgICAgICAgICAgICAgICAgICAgXCIqXCIgLyBcIitcIiAvIFwiLVwiIC8gXCIuXCIgLyBcIl5cIiAvIFwiX1wiIC9cblx0ICogICAgICAgICAgICAgICAgICAgICBcImBcIiAvIFwifFwiIC8gXCJ+XCIgLyBESUdJVCAvIEFMUEhBXG5cdCAqL1xuXG5cdHZhciBjb29raWVOYW1lUmVnRXhwID0gL15bISMkJSYnKitcXC0uXl9gfH4wLTlBLVphLXpdKyQvO1xuXG5cdC8qKlxuXHQgKiBSZWdFeHAgdG8gbWF0Y2ggY29va2llLXZhbHVlIGluIFJGQyA2MjY1IHNlYyA0LjEuMVxuXHQgKlxuXHQgKiBjb29raWUtdmFsdWUgICAgICA9ICpjb29raWUtb2N0ZXQgLyAoIERRVU9URSAqY29va2llLW9jdGV0IERRVU9URSApXG5cdCAqIGNvb2tpZS1vY3RldCAgICAgID0gJXgyMSAvICV4MjMtMkIgLyAleDJELTNBIC8gJXgzQy01QiAvICV4NUQtN0Vcblx0ICogICAgICAgICAgICAgICAgICAgICA7IFVTLUFTQ0lJIGNoYXJhY3RlcnMgZXhjbHVkaW5nIENUTHMsXG5cdCAqICAgICAgICAgICAgICAgICAgICAgOyB3aGl0ZXNwYWNlIERRVU9URSwgY29tbWEsIHNlbWljb2xvbixcblx0ICogICAgICAgICAgICAgICAgICAgICA7IGFuZCBiYWNrc2xhc2hcblx0ICovXG5cblx0dmFyIGNvb2tpZVZhbHVlUmVnRXhwID0gL14oXCI/KVtcXHUwMDIxXFx1MDAyMy1cXHUwMDJCXFx1MDAyRC1cXHUwMDNBXFx1MDAzQy1cXHUwMDVCXFx1MDA1RC1cXHUwMDdFXSpcXDEkLztcblxuXHQvKipcblx0ICogUmVnRXhwIHRvIG1hdGNoIGRvbWFpbi12YWx1ZSBpbiBSRkMgNjI2NSBzZWMgNC4xLjFcblx0ICpcblx0ICogZG9tYWluLXZhbHVlICAgICAgPSA8c3ViZG9tYWluPlxuXHQgKiAgICAgICAgICAgICAgICAgICAgIDsgZGVmaW5lZCBpbiBbUkZDMTAzNF0sIFNlY3Rpb24gMy41LCBhc1xuXHQgKiAgICAgICAgICAgICAgICAgICAgIDsgZW5oYW5jZWQgYnkgW1JGQzExMjNdLCBTZWN0aW9uIDIuMVxuXHQgKiA8c3ViZG9tYWluPiAgICAgICA9IDxsYWJlbD4gfCA8c3ViZG9tYWluPiBcIi5cIiA8bGFiZWw+XG5cdCAqIDxsYWJlbD4gICAgICAgICAgID0gPGxldC1kaWc+IFsgWyA8bGRoLXN0cj4gXSA8bGV0LWRpZz4gXVxuXHQgKiAgICAgICAgICAgICAgICAgICAgIExhYmVscyBtdXN0IGJlIDYzIGNoYXJhY3RlcnMgb3IgbGVzcy5cblx0ICogICAgICAgICAgICAgICAgICAgICAnbGV0LWRpZycgbm90ICdsZXR0ZXInIGluIHRoZSBmaXJzdCBjaGFyLCBwZXIgUkZDMTEyM1xuXHQgKiA8bGRoLXN0cj4gICAgICAgICA9IDxsZXQtZGlnLWh5cD4gfCA8bGV0LWRpZy1oeXA+IDxsZGgtc3RyPlxuXHQgKiA8bGV0LWRpZy1oeXA+ICAgICA9IDxsZXQtZGlnPiB8IFwiLVwiXG5cdCAqIDxsZXQtZGlnPiAgICAgICAgID0gPGxldHRlcj4gfCA8ZGlnaXQ+XG5cdCAqIDxsZXR0ZXI+ICAgICAgICAgID0gYW55IG9uZSBvZiB0aGUgNTIgYWxwaGFiZXRpYyBjaGFyYWN0ZXJzIEEgdGhyb3VnaCBaIGluXG5cdCAqICAgICAgICAgICAgICAgICAgICAgdXBwZXIgY2FzZSBhbmQgYSB0aHJvdWdoIHogaW4gbG93ZXIgY2FzZVxuXHQgKiA8ZGlnaXQ+ICAgICAgICAgICA9IGFueSBvbmUgb2YgdGhlIHRlbiBkaWdpdHMgMCB0aHJvdWdoIDlcblx0ICpcblx0ICogS2VlcCBzdXBwb3J0IGZvciBsZWFkaW5nIGRvdDogaHR0cHM6Ly9naXRodWIuY29tL2pzaHR0cC9jb29raWUvaXNzdWVzLzE3M1xuXHQgKlxuXHQgKiA+IChOb3RlIHRoYXQgYSBsZWFkaW5nICV4MkUgKFwiLlwiKSwgaWYgcHJlc2VudCwgaXMgaWdub3JlZCBldmVuIHRob3VnaCB0aGF0XG5cdCAqIGNoYXJhY3RlciBpcyBub3QgcGVybWl0dGVkLCBidXQgYSB0cmFpbGluZyAleDJFIChcIi5cIiksIGlmIHByZXNlbnQsIHdpbGxcblx0ICogY2F1c2UgdGhlIHVzZXIgYWdlbnQgdG8gaWdub3JlIHRoZSBhdHRyaWJ1dGUuKVxuXHQgKi9cblxuXHR2YXIgZG9tYWluVmFsdWVSZWdFeHAgPSAvXihbLl0/W2EtejAtOV0oW2EtejAtOS1dezAsNjF9W2EtejAtOV0pPykoWy5dW2EtejAtOV0oW2EtejAtOS1dezAsNjF9W2EtejAtOV0pPykqJC9pO1xuXG5cdC8qKlxuXHQgKiBSZWdFeHAgdG8gbWF0Y2ggcGF0aC12YWx1ZSBpbiBSRkMgNjI2NSBzZWMgNC4xLjFcblx0ICpcblx0ICogcGF0aC12YWx1ZSAgICAgICAgPSA8YW55IENIQVIgZXhjZXB0IENUTHMgb3IgXCI7XCI+XG5cdCAqIENIQVIgICAgICAgICAgICAgID0gJXgwMS03RlxuXHQgKiAgICAgICAgICAgICAgICAgICAgIDsgZGVmaW5lZCBpbiBSRkMgNTIzNCBhcHBlbmRpeCBCLjFcblx0ICovXG5cblx0dmFyIHBhdGhWYWx1ZVJlZ0V4cCA9IC9eW1xcdTAwMjAtXFx1MDAzQVxcdTAwM0QtXFx1MDA3RV0qJC87XG5cblx0LyoqXG5cdCAqIFBhcnNlIGEgY29va2llIGhlYWRlci5cblx0ICpcblx0ICogUGFyc2UgdGhlIGdpdmVuIGNvb2tpZSBoZWFkZXIgc3RyaW5nIGludG8gYW4gb2JqZWN0XG5cdCAqIFRoZSBvYmplY3QgaGFzIHRoZSB2YXJpb3VzIGNvb2tpZXMgYXMga2V5cyhuYW1lcykgPT4gdmFsdWVzXG5cdCAqXG5cdCAqIEBwYXJhbSB7c3RyaW5nfSBzdHJcblx0ICogQHBhcmFtIHtvYmplY3R9IFtvcHRdXG5cdCAqIEByZXR1cm4ge29iamVjdH1cblx0ICogQHB1YmxpY1xuXHQgKi9cblxuXHRmdW5jdGlvbiBwYXJzZShzdHIsIG9wdCkge1xuXHQgIGlmICh0eXBlb2Ygc3RyICE9PSAnc3RyaW5nJykge1xuXHQgICAgdGhyb3cgbmV3IFR5cGVFcnJvcignYXJndW1lbnQgc3RyIG11c3QgYmUgYSBzdHJpbmcnKTtcblx0ICB9XG5cblx0ICB2YXIgb2JqID0ge307XG5cdCAgdmFyIGxlbiA9IHN0ci5sZW5ndGg7XG5cdCAgLy8gUkZDIDYyNjUgc2VjIDQuMS4xLCBSRkMgMjYxNiAyLjIgZGVmaW5lcyBhIGNvb2tpZSBuYW1lIGNvbnNpc3RzIG9mIG9uZSBjaGFyIG1pbmltdW0sIHBsdXMgJz0nLlxuXHQgIGlmIChsZW4gPCAyKSByZXR1cm4gb2JqO1xuXG5cdCAgdmFyIGRlYyA9IChvcHQgJiYgb3B0LmRlY29kZSkgfHwgZGVjb2RlO1xuXHQgIHZhciBpbmRleCA9IDA7XG5cdCAgdmFyIGVxSWR4ID0gMDtcblx0ICB2YXIgZW5kSWR4ID0gMDtcblxuXHQgIGRvIHtcblx0ICAgIGVxSWR4ID0gc3RyLmluZGV4T2YoJz0nLCBpbmRleCk7XG5cdCAgICBpZiAoZXFJZHggPT09IC0xKSBicmVhazsgLy8gTm8gbW9yZSBjb29raWUgcGFpcnMuXG5cblx0ICAgIGVuZElkeCA9IHN0ci5pbmRleE9mKCc7JywgaW5kZXgpO1xuXG5cdCAgICBpZiAoZW5kSWR4ID09PSAtMSkge1xuXHQgICAgICBlbmRJZHggPSBsZW47XG5cdCAgICB9IGVsc2UgaWYgKGVxSWR4ID4gZW5kSWR4KSB7XG5cdCAgICAgIC8vIGJhY2t0cmFjayBvbiBwcmlvciBzZW1pY29sb25cblx0ICAgICAgaW5kZXggPSBzdHIubGFzdEluZGV4T2YoJzsnLCBlcUlkeCAtIDEpICsgMTtcblx0ICAgICAgY29udGludWU7XG5cdCAgICB9XG5cblx0ICAgIHZhciBrZXlTdGFydElkeCA9IHN0YXJ0SW5kZXgoc3RyLCBpbmRleCwgZXFJZHgpO1xuXHQgICAgdmFyIGtleUVuZElkeCA9IGVuZEluZGV4KHN0ciwgZXFJZHgsIGtleVN0YXJ0SWR4KTtcblx0ICAgIHZhciBrZXkgPSBzdHIuc2xpY2Uoa2V5U3RhcnRJZHgsIGtleUVuZElkeCk7XG5cblx0ICAgIC8vIG9ubHkgYXNzaWduIG9uY2Vcblx0ICAgIGlmICghX19oYXNPd25Qcm9wZXJ0eS5jYWxsKG9iaiwga2V5KSkge1xuXHQgICAgICB2YXIgdmFsU3RhcnRJZHggPSBzdGFydEluZGV4KHN0ciwgZXFJZHggKyAxLCBlbmRJZHgpO1xuXHQgICAgICB2YXIgdmFsRW5kSWR4ID0gZW5kSW5kZXgoc3RyLCBlbmRJZHgsIHZhbFN0YXJ0SWR4KTtcblxuXHQgICAgICBpZiAoc3RyLmNoYXJDb2RlQXQodmFsU3RhcnRJZHgpID09PSAweDIyIC8qIFwiICovICYmIHN0ci5jaGFyQ29kZUF0KHZhbEVuZElkeCAtIDEpID09PSAweDIyIC8qIFwiICovKSB7XG5cdCAgICAgICAgdmFsU3RhcnRJZHgrKztcblx0ICAgICAgICB2YWxFbmRJZHgtLTtcblx0ICAgICAgfVxuXG5cdCAgICAgIHZhciB2YWwgPSBzdHIuc2xpY2UodmFsU3RhcnRJZHgsIHZhbEVuZElkeCk7XG5cdCAgICAgIG9ialtrZXldID0gdHJ5RGVjb2RlKHZhbCwgZGVjKTtcblx0ICAgIH1cblxuXHQgICAgaW5kZXggPSBlbmRJZHggKyAxO1xuXHQgIH0gd2hpbGUgKGluZGV4IDwgbGVuKTtcblxuXHQgIHJldHVybiBvYmo7XG5cdH1cblxuXHRmdW5jdGlvbiBzdGFydEluZGV4KHN0ciwgaW5kZXgsIG1heCkge1xuXHQgIGRvIHtcblx0ICAgIHZhciBjb2RlID0gc3RyLmNoYXJDb2RlQXQoaW5kZXgpO1xuXHQgICAgaWYgKGNvZGUgIT09IDB4MjAgLyogICAqLyAmJiBjb2RlICE9PSAweDA5IC8qIFxcdCAqLykgcmV0dXJuIGluZGV4O1xuXHQgIH0gd2hpbGUgKCsraW5kZXggPCBtYXgpO1xuXHQgIHJldHVybiBtYXg7XG5cdH1cblxuXHRmdW5jdGlvbiBlbmRJbmRleChzdHIsIGluZGV4LCBtaW4pIHtcblx0ICB3aGlsZSAoaW5kZXggPiBtaW4pIHtcblx0ICAgIHZhciBjb2RlID0gc3RyLmNoYXJDb2RlQXQoLS1pbmRleCk7XG5cdCAgICBpZiAoY29kZSAhPT0gMHgyMCAvKiAgICovICYmIGNvZGUgIT09IDB4MDkgLyogXFx0ICovKSByZXR1cm4gaW5kZXggKyAxO1xuXHQgIH1cblx0ICByZXR1cm4gbWluO1xuXHR9XG5cblx0LyoqXG5cdCAqIFNlcmlhbGl6ZSBkYXRhIGludG8gYSBjb29raWUgaGVhZGVyLlxuXHQgKlxuXHQgKiBTZXJpYWxpemUgYSBuYW1lIHZhbHVlIHBhaXIgaW50byBhIGNvb2tpZSBzdHJpbmcgc3VpdGFibGUgZm9yXG5cdCAqIGh0dHAgaGVhZGVycy4gQW4gb3B0aW9uYWwgb3B0aW9ucyBvYmplY3Qgc3BlY2lmaWVzIGNvb2tpZSBwYXJhbWV0ZXJzLlxuXHQgKlxuXHQgKiBzZXJpYWxpemUoJ2ZvbycsICdiYXInLCB7IGh0dHBPbmx5OiB0cnVlIH0pXG5cdCAqICAgPT4gXCJmb289YmFyOyBodHRwT25seVwiXG5cdCAqXG5cdCAqIEBwYXJhbSB7c3RyaW5nfSBuYW1lXG5cdCAqIEBwYXJhbSB7c3RyaW5nfSB2YWxcblx0ICogQHBhcmFtIHtvYmplY3R9IFtvcHRdXG5cdCAqIEByZXR1cm4ge3N0cmluZ31cblx0ICogQHB1YmxpY1xuXHQgKi9cblxuXHRmdW5jdGlvbiBzZXJpYWxpemUobmFtZSwgdmFsLCBvcHQpIHtcblx0ICB2YXIgZW5jID0gKG9wdCAmJiBvcHQuZW5jb2RlKSB8fCBlbmNvZGVVUklDb21wb25lbnQ7XG5cblx0ICBpZiAodHlwZW9mIGVuYyAhPT0gJ2Z1bmN0aW9uJykge1xuXHQgICAgdGhyb3cgbmV3IFR5cGVFcnJvcignb3B0aW9uIGVuY29kZSBpcyBpbnZhbGlkJyk7XG5cdCAgfVxuXG5cdCAgaWYgKCFjb29raWVOYW1lUmVnRXhwLnRlc3QobmFtZSkpIHtcblx0ICAgIHRocm93IG5ldyBUeXBlRXJyb3IoJ2FyZ3VtZW50IG5hbWUgaXMgaW52YWxpZCcpO1xuXHQgIH1cblxuXHQgIHZhciB2YWx1ZSA9IGVuYyh2YWwpO1xuXG5cdCAgaWYgKCFjb29raWVWYWx1ZVJlZ0V4cC50ZXN0KHZhbHVlKSkge1xuXHQgICAgdGhyb3cgbmV3IFR5cGVFcnJvcignYXJndW1lbnQgdmFsIGlzIGludmFsaWQnKTtcblx0ICB9XG5cblx0ICB2YXIgc3RyID0gbmFtZSArICc9JyArIHZhbHVlO1xuXHQgIGlmICghb3B0KSByZXR1cm4gc3RyO1xuXG5cdCAgaWYgKG51bGwgIT0gb3B0Lm1heEFnZSkge1xuXHQgICAgdmFyIG1heEFnZSA9IE1hdGguZmxvb3Iob3B0Lm1heEFnZSk7XG5cblx0ICAgIGlmICghaXNGaW5pdGUobWF4QWdlKSkge1xuXHQgICAgICB0aHJvdyBuZXcgVHlwZUVycm9yKCdvcHRpb24gbWF4QWdlIGlzIGludmFsaWQnKVxuXHQgICAgfVxuXG5cdCAgICBzdHIgKz0gJzsgTWF4LUFnZT0nICsgbWF4QWdlO1xuXHQgIH1cblxuXHQgIGlmIChvcHQuZG9tYWluKSB7XG5cdCAgICBpZiAoIWRvbWFpblZhbHVlUmVnRXhwLnRlc3Qob3B0LmRvbWFpbikpIHtcblx0ICAgICAgdGhyb3cgbmV3IFR5cGVFcnJvcignb3B0aW9uIGRvbWFpbiBpcyBpbnZhbGlkJyk7XG5cdCAgICB9XG5cblx0ICAgIHN0ciArPSAnOyBEb21haW49JyArIG9wdC5kb21haW47XG5cdCAgfVxuXG5cdCAgaWYgKG9wdC5wYXRoKSB7XG5cdCAgICBpZiAoIXBhdGhWYWx1ZVJlZ0V4cC50ZXN0KG9wdC5wYXRoKSkge1xuXHQgICAgICB0aHJvdyBuZXcgVHlwZUVycm9yKCdvcHRpb24gcGF0aCBpcyBpbnZhbGlkJyk7XG5cdCAgICB9XG5cblx0ICAgIHN0ciArPSAnOyBQYXRoPScgKyBvcHQucGF0aDtcblx0ICB9XG5cblx0ICBpZiAob3B0LmV4cGlyZXMpIHtcblx0ICAgIHZhciBleHBpcmVzID0gb3B0LmV4cGlyZXM7XG5cblx0ICAgIGlmICghaXNEYXRlKGV4cGlyZXMpIHx8IGlzTmFOKGV4cGlyZXMudmFsdWVPZigpKSkge1xuXHQgICAgICB0aHJvdyBuZXcgVHlwZUVycm9yKCdvcHRpb24gZXhwaXJlcyBpcyBpbnZhbGlkJyk7XG5cdCAgICB9XG5cblx0ICAgIHN0ciArPSAnOyBFeHBpcmVzPScgKyBleHBpcmVzLnRvVVRDU3RyaW5nKCk7XG5cdCAgfVxuXG5cdCAgaWYgKG9wdC5odHRwT25seSkge1xuXHQgICAgc3RyICs9ICc7IEh0dHBPbmx5Jztcblx0ICB9XG5cblx0ICBpZiAob3B0LnNlY3VyZSkge1xuXHQgICAgc3RyICs9ICc7IFNlY3VyZSc7XG5cdCAgfVxuXG5cdCAgaWYgKG9wdC5wYXJ0aXRpb25lZCkge1xuXHQgICAgc3RyICs9ICc7IFBhcnRpdGlvbmVkJztcblx0ICB9XG5cblx0ICBpZiAob3B0LnByaW9yaXR5KSB7XG5cdCAgICB2YXIgcHJpb3JpdHkgPSB0eXBlb2Ygb3B0LnByaW9yaXR5ID09PSAnc3RyaW5nJ1xuXHQgICAgICA/IG9wdC5wcmlvcml0eS50b0xvd2VyQ2FzZSgpIDogb3B0LnByaW9yaXR5O1xuXG5cdCAgICBzd2l0Y2ggKHByaW9yaXR5KSB7XG5cdCAgICAgIGNhc2UgJ2xvdyc6XG5cdCAgICAgICAgc3RyICs9ICc7IFByaW9yaXR5PUxvdyc7XG5cdCAgICAgICAgYnJlYWtcblx0ICAgICAgY2FzZSAnbWVkaXVtJzpcblx0ICAgICAgICBzdHIgKz0gJzsgUHJpb3JpdHk9TWVkaXVtJztcblx0ICAgICAgICBicmVha1xuXHQgICAgICBjYXNlICdoaWdoJzpcblx0ICAgICAgICBzdHIgKz0gJzsgUHJpb3JpdHk9SGlnaCc7XG5cdCAgICAgICAgYnJlYWtcblx0ICAgICAgZGVmYXVsdDpcblx0ICAgICAgICB0aHJvdyBuZXcgVHlwZUVycm9yKCdvcHRpb24gcHJpb3JpdHkgaXMgaW52YWxpZCcpXG5cdCAgICB9XG5cdCAgfVxuXG5cdCAgaWYgKG9wdC5zYW1lU2l0ZSkge1xuXHQgICAgdmFyIHNhbWVTaXRlID0gdHlwZW9mIG9wdC5zYW1lU2l0ZSA9PT0gJ3N0cmluZydcblx0ICAgICAgPyBvcHQuc2FtZVNpdGUudG9Mb3dlckNhc2UoKSA6IG9wdC5zYW1lU2l0ZTtcblxuXHQgICAgc3dpdGNoIChzYW1lU2l0ZSkge1xuXHQgICAgICBjYXNlIHRydWU6XG5cdCAgICAgICAgc3RyICs9ICc7IFNhbWVTaXRlPVN0cmljdCc7XG5cdCAgICAgICAgYnJlYWs7XG5cdCAgICAgIGNhc2UgJ2xheCc6XG5cdCAgICAgICAgc3RyICs9ICc7IFNhbWVTaXRlPUxheCc7XG5cdCAgICAgICAgYnJlYWs7XG5cdCAgICAgIGNhc2UgJ3N0cmljdCc6XG5cdCAgICAgICAgc3RyICs9ICc7IFNhbWVTaXRlPVN0cmljdCc7XG5cdCAgICAgICAgYnJlYWs7XG5cdCAgICAgIGNhc2UgJ25vbmUnOlxuXHQgICAgICAgIHN0ciArPSAnOyBTYW1lU2l0ZT1Ob25lJztcblx0ICAgICAgICBicmVhaztcblx0ICAgICAgZGVmYXVsdDpcblx0ICAgICAgICB0aHJvdyBuZXcgVHlwZUVycm9yKCdvcHRpb24gc2FtZVNpdGUgaXMgaW52YWxpZCcpO1xuXHQgICAgfVxuXHQgIH1cblxuXHQgIHJldHVybiBzdHI7XG5cdH1cblxuXHQvKipcblx0ICogVVJMLWRlY29kZSBzdHJpbmcgdmFsdWUuIE9wdGltaXplZCB0byBza2lwIG5hdGl2ZSBjYWxsIHdoZW4gbm8gJS5cblx0ICpcblx0ICogQHBhcmFtIHtzdHJpbmd9IHN0clxuXHQgKiBAcmV0dXJucyB7c3RyaW5nfVxuXHQgKi9cblxuXHRmdW5jdGlvbiBkZWNvZGUgKHN0cikge1xuXHQgIHJldHVybiBzdHIuaW5kZXhPZignJScpICE9PSAtMVxuXHQgICAgPyBkZWNvZGVVUklDb21wb25lbnQoc3RyKVxuXHQgICAgOiBzdHJcblx0fVxuXG5cdC8qKlxuXHQgKiBEZXRlcm1pbmUgaWYgdmFsdWUgaXMgYSBEYXRlLlxuXHQgKlxuXHQgKiBAcGFyYW0geyp9IHZhbFxuXHQgKiBAcHJpdmF0ZVxuXHQgKi9cblxuXHRmdW5jdGlvbiBpc0RhdGUgKHZhbCkge1xuXHQgIHJldHVybiBfX3RvU3RyaW5nLmNhbGwodmFsKSA9PT0gJ1tvYmplY3QgRGF0ZV0nO1xuXHR9XG5cblx0LyoqXG5cdCAqIFRyeSBkZWNvZGluZyBhIHN0cmluZyB1c2luZyBhIGRlY29kaW5nIGZ1bmN0aW9uLlxuXHQgKlxuXHQgKiBAcGFyYW0ge3N0cmluZ30gc3RyXG5cdCAqIEBwYXJhbSB7ZnVuY3Rpb259IGRlY29kZVxuXHQgKiBAcHJpdmF0ZVxuXHQgKi9cblxuXHRmdW5jdGlvbiB0cnlEZWNvZGUoc3RyLCBkZWNvZGUpIHtcblx0ICB0cnkge1xuXHQgICAgcmV0dXJuIGRlY29kZShzdHIpO1xuXHQgIH0gY2F0Y2ggKGUpIHtcblx0ICAgIHJldHVybiBzdHI7XG5cdCAgfVxuXHR9XG5cdHJldHVybiBjb29raWU7XG59XG5cbnZhciBjb29raWVFeHBvcnRzID0gcmVxdWlyZUNvb2tpZSgpO1xuXG5mdW5jdGlvbiBoYXNEb2N1bWVudENvb2tpZSgpIHtcbiAgICBjb25zdCB0ZXN0aW5nVmFsdWUgPSB0eXBlb2YgZ2xvYmFsID09PSAndW5kZWZpbmVkJ1xuICAgICAgICA/IHVuZGVmaW5lZFxuICAgICAgICA6IGdsb2JhbC5URVNUX0hBU19ET0NVTUVOVF9DT09LSUU7XG4gICAgaWYgKHR5cGVvZiB0ZXN0aW5nVmFsdWUgPT09ICdib29sZWFuJykge1xuICAgICAgICByZXR1cm4gdGVzdGluZ1ZhbHVlO1xuICAgIH1cbiAgICAvLyBDYW4gd2UgZ2V0L3NldCBjb29raWVzIG9uIGRvY3VtZW50LmNvb2tpZT9cbiAgICByZXR1cm4gdHlwZW9mIGRvY3VtZW50ID09PSAnb2JqZWN0JyAmJiB0eXBlb2YgZG9jdW1lbnQuY29va2llID09PSAnc3RyaW5nJztcbn1cbmZ1bmN0aW9uIHBhcnNlQ29va2llcyhjb29raWVzKSB7XG4gICAgaWYgKHR5cGVvZiBjb29raWVzID09PSAnc3RyaW5nJykge1xuICAgICAgICByZXR1cm4gY29va2llRXhwb3J0cy5wYXJzZShjb29raWVzKTtcbiAgICB9XG4gICAgZWxzZSBpZiAodHlwZW9mIGNvb2tpZXMgPT09ICdvYmplY3QnICYmIGNvb2tpZXMgIT09IG51bGwpIHtcbiAgICAgICAgcmV0dXJuIGNvb2tpZXM7XG4gICAgfVxuICAgIGVsc2Uge1xuICAgICAgICByZXR1cm4ge307XG4gICAgfVxufVxuZnVuY3Rpb24gcmVhZENvb2tpZSh2YWx1ZSwgb3B0aW9ucyA9IHt9KSB7XG4gICAgY29uc3QgY2xlYW5WYWx1ZSA9IGNsZWFudXBDb29raWVWYWx1ZSh2YWx1ZSk7XG4gICAgaWYgKCFvcHRpb25zLmRvTm90UGFyc2UpIHtcbiAgICAgICAgdHJ5IHtcbiAgICAgICAgICAgIHJldHVybiBKU09OLnBhcnNlKGNsZWFuVmFsdWUpO1xuICAgICAgICB9XG4gICAgICAgIGNhdGNoIChlKSB7XG4gICAgICAgICAgICAvLyBBdCBsZWFzdCB3ZSB0cmllZFxuICAgICAgICB9XG4gICAgfVxuICAgIC8vIElnbm9yZSBjbGVhbiB2YWx1ZSBpZiB3ZSBmYWlsZWQgdGhlIGRlc2VyaWFsaXphdGlvblxuICAgIC8vIEl0IGlzIG5vdCByZWxldmFudCBhbnltb3JlIHRvIHRyaW0gdGhvc2UgdmFsdWVzXG4gICAgcmV0dXJuIHZhbHVlO1xufVxuZnVuY3Rpb24gY2xlYW51cENvb2tpZVZhbHVlKHZhbHVlKSB7XG4gICAgLy8gZXhwcmVzcyBwcmVwZW5kIGo6IGJlZm9yZSBzZXJpYWxpemluZyBhIGNvb2tpZVxuICAgIGlmICh2YWx1ZSAmJiB2YWx1ZVswXSA9PT0gJ2onICYmIHZhbHVlWzFdID09PSAnOicpIHtcbiAgICAgICAgcmV0dXJuIHZhbHVlLnN1YnN0cigyKTtcbiAgICB9XG4gICAgcmV0dXJuIHZhbHVlO1xufVxuXG5jbGFzcyBDb29raWVzIHtcbiAgICBjb25zdHJ1Y3Rvcihjb29raWVzLCBkZWZhdWx0U2V0T3B0aW9ucyA9IHt9KSB7XG4gICAgICAgIHRoaXMuY2hhbmdlTGlzdGVuZXJzID0gW107XG4gICAgICAgIHRoaXMuSEFTX0RPQ1VNRU5UX0NPT0tJRSA9IGZhbHNlO1xuICAgICAgICB0aGlzLnVwZGF0ZSA9ICgpID0+IHtcbiAgICAgICAgICAgIGlmICghdGhpcy5IQVNfRE9DVU1FTlRfQ09PS0lFKSB7XG4gICAgICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgY29uc3QgcHJldmlvdXNDb29raWVzID0gdGhpcy5jb29raWVzO1xuICAgICAgICAgICAgdGhpcy5jb29raWVzID0gY29va2llRXhwb3J0cy5wYXJzZShkb2N1bWVudC5jb29raWUpO1xuICAgICAgICAgICAgdGhpcy5fY2hlY2tDaGFuZ2VzKHByZXZpb3VzQ29va2llcyk7XG4gICAgICAgIH07XG4gICAgICAgIGNvbnN0IGRvbUNvb2tpZXMgPSB0eXBlb2YgZG9jdW1lbnQgPT09ICd1bmRlZmluZWQnID8gJycgOiBkb2N1bWVudC5jb29raWU7XG4gICAgICAgIHRoaXMuY29va2llcyA9IHBhcnNlQ29va2llcyhjb29raWVzIHx8IGRvbUNvb2tpZXMpO1xuICAgICAgICB0aGlzLmRlZmF1bHRTZXRPcHRpb25zID0gZGVmYXVsdFNldE9wdGlvbnM7XG4gICAgICAgIHRoaXMuSEFTX0RPQ1VNRU5UX0NPT0tJRSA9IGhhc0RvY3VtZW50Q29va2llKCk7XG4gICAgfVxuICAgIF9lbWl0Q2hhbmdlKHBhcmFtcykge1xuICAgICAgICBmb3IgKGxldCBpID0gMDsgaSA8IHRoaXMuY2hhbmdlTGlzdGVuZXJzLmxlbmd0aDsgKytpKSB7XG4gICAgICAgICAgICB0aGlzLmNoYW5nZUxpc3RlbmVyc1tpXShwYXJhbXMpO1xuICAgICAgICB9XG4gICAgfVxuICAgIF9jaGVja0NoYW5nZXMocHJldmlvdXNDb29raWVzKSB7XG4gICAgICAgIGNvbnN0IG5hbWVzID0gbmV3IFNldChPYmplY3Qua2V5cyhwcmV2aW91c0Nvb2tpZXMpLmNvbmNhdChPYmplY3Qua2V5cyh0aGlzLmNvb2tpZXMpKSk7XG4gICAgICAgIG5hbWVzLmZvckVhY2goKG5hbWUpID0+IHtcbiAgICAgICAgICAgIGlmIChwcmV2aW91c0Nvb2tpZXNbbmFtZV0gIT09IHRoaXMuY29va2llc1tuYW1lXSkge1xuICAgICAgICAgICAgICAgIHRoaXMuX2VtaXRDaGFuZ2Uoe1xuICAgICAgICAgICAgICAgICAgICBuYW1lLFxuICAgICAgICAgICAgICAgICAgICB2YWx1ZTogcmVhZENvb2tpZSh0aGlzLmNvb2tpZXNbbmFtZV0pLFxuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICB9XG4gICAgX3N0YXJ0UG9sbGluZygpIHtcbiAgICAgICAgdGhpcy5wb2xsaW5nSW50ZXJ2YWwgPSBzZXRJbnRlcnZhbCh0aGlzLnVwZGF0ZSwgMzAwKTtcbiAgICB9XG4gICAgX3N0b3BQb2xsaW5nKCkge1xuICAgICAgICBpZiAodGhpcy5wb2xsaW5nSW50ZXJ2YWwpIHtcbiAgICAgICAgICAgIGNsZWFySW50ZXJ2YWwodGhpcy5wb2xsaW5nSW50ZXJ2YWwpO1xuICAgICAgICB9XG4gICAgfVxuICAgIGdldChuYW1lLCBvcHRpb25zID0ge30pIHtcbiAgICAgICAgaWYgKCFvcHRpb25zLmRvTm90VXBkYXRlKSB7XG4gICAgICAgICAgICB0aGlzLnVwZGF0ZSgpO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiByZWFkQ29va2llKHRoaXMuY29va2llc1tuYW1lXSwgb3B0aW9ucyk7XG4gICAgfVxuICAgIGdldEFsbChvcHRpb25zID0ge30pIHtcbiAgICAgICAgaWYgKCFvcHRpb25zLmRvTm90VXBkYXRlKSB7XG4gICAgICAgICAgICB0aGlzLnVwZGF0ZSgpO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHJlc3VsdCA9IHt9O1xuICAgICAgICBmb3IgKGxldCBuYW1lIGluIHRoaXMuY29va2llcykge1xuICAgICAgICAgICAgcmVzdWx0W25hbWVdID0gcmVhZENvb2tpZSh0aGlzLmNvb2tpZXNbbmFtZV0sIG9wdGlvbnMpO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiByZXN1bHQ7XG4gICAgfVxuICAgIHNldChuYW1lLCB2YWx1ZSwgb3B0aW9ucykge1xuICAgICAgICBpZiAob3B0aW9ucykge1xuICAgICAgICAgICAgb3B0aW9ucyA9IE9iamVjdC5hc3NpZ24oT2JqZWN0LmFzc2lnbih7fSwgdGhpcy5kZWZhdWx0U2V0T3B0aW9ucyksIG9wdGlvbnMpO1xuICAgICAgICB9XG4gICAgICAgIGVsc2Uge1xuICAgICAgICAgICAgb3B0aW9ucyA9IHRoaXMuZGVmYXVsdFNldE9wdGlvbnM7XG4gICAgICAgIH1cbiAgICAgICAgY29uc3Qgc3RyaW5nVmFsdWUgPSB0eXBlb2YgdmFsdWUgPT09ICdzdHJpbmcnID8gdmFsdWUgOiBKU09OLnN0cmluZ2lmeSh2YWx1ZSk7XG4gICAgICAgIHRoaXMuY29va2llcyA9IE9iamVjdC5hc3NpZ24oT2JqZWN0LmFzc2lnbih7fSwgdGhpcy5jb29raWVzKSwgeyBbbmFtZV06IHN0cmluZ1ZhbHVlIH0pO1xuICAgICAgICBpZiAodGhpcy5IQVNfRE9DVU1FTlRfQ09PS0lFKSB7XG4gICAgICAgICAgICBkb2N1bWVudC5jb29raWUgPSBjb29raWVFeHBvcnRzLnNlcmlhbGl6ZShuYW1lLCBzdHJpbmdWYWx1ZSwgb3B0aW9ucyk7XG4gICAgICAgIH1cbiAgICAgICAgdGhpcy5fZW1pdENoYW5nZSh7IG5hbWUsIHZhbHVlLCBvcHRpb25zIH0pO1xuICAgIH1cbiAgICByZW1vdmUobmFtZSwgb3B0aW9ucykge1xuICAgICAgICBjb25zdCBmaW5hbE9wdGlvbnMgPSAob3B0aW9ucyA9IE9iamVjdC5hc3NpZ24oT2JqZWN0LmFzc2lnbihPYmplY3QuYXNzaWduKHt9LCB0aGlzLmRlZmF1bHRTZXRPcHRpb25zKSwgb3B0aW9ucyksIHsgZXhwaXJlczogbmV3IERhdGUoMTk3MCwgMSwgMSwgMCwgMCwgMSksIG1heEFnZTogMCB9KSk7XG4gICAgICAgIHRoaXMuY29va2llcyA9IE9iamVjdC5hc3NpZ24oe30sIHRoaXMuY29va2llcyk7XG4gICAgICAgIGRlbGV0ZSB0aGlzLmNvb2tpZXNbbmFtZV07XG4gICAgICAgIGlmICh0aGlzLkhBU19ET0NVTUVOVF9DT09LSUUpIHtcbiAgICAgICAgICAgIGRvY3VtZW50LmNvb2tpZSA9IGNvb2tpZUV4cG9ydHMuc2VyaWFsaXplKG5hbWUsICcnLCBmaW5hbE9wdGlvbnMpO1xuICAgICAgICB9XG4gICAgICAgIHRoaXMuX2VtaXRDaGFuZ2UoeyBuYW1lLCB2YWx1ZTogdW5kZWZpbmVkLCBvcHRpb25zIH0pO1xuICAgIH1cbiAgICBhZGRDaGFuZ2VMaXN0ZW5lcihjYWxsYmFjaykge1xuICAgICAgICB0aGlzLmNoYW5nZUxpc3RlbmVycy5wdXNoKGNhbGxiYWNrKTtcbiAgICAgICAgaWYgKHRoaXMuSEFTX0RPQ1VNRU5UX0NPT0tJRSAmJiB0aGlzLmNoYW5nZUxpc3RlbmVycy5sZW5ndGggPT09IDEpIHtcbiAgICAgICAgICAgIGlmICh0eXBlb2Ygd2luZG93ID09PSAnb2JqZWN0JyAmJiAnY29va2llU3RvcmUnIGluIHdpbmRvdykge1xuICAgICAgICAgICAgICAgIHdpbmRvdy5jb29raWVTdG9yZS5hZGRFdmVudExpc3RlbmVyKCdjaGFuZ2UnLCB0aGlzLnVwZGF0ZSk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICBlbHNlIHtcbiAgICAgICAgICAgICAgICB0aGlzLl9zdGFydFBvbGxpbmcoKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH1cbiAgICByZW1vdmVDaGFuZ2VMaXN0ZW5lcihjYWxsYmFjaykge1xuICAgICAgICBjb25zdCBpZHggPSB0aGlzLmNoYW5nZUxpc3RlbmVycy5pbmRleE9mKGNhbGxiYWNrKTtcbiAgICAgICAgaWYgKGlkeCA+PSAwKSB7XG4gICAgICAgICAgICB0aGlzLmNoYW5nZUxpc3RlbmVycy5zcGxpY2UoaWR4LCAxKTtcbiAgICAgICAgfVxuICAgICAgICBpZiAodGhpcy5IQVNfRE9DVU1FTlRfQ09PS0lFICYmIHRoaXMuY2hhbmdlTGlzdGVuZXJzLmxlbmd0aCA9PT0gMCkge1xuICAgICAgICAgICAgaWYgKHR5cGVvZiB3aW5kb3cgPT09ICdvYmplY3QnICYmICdjb29raWVTdG9yZScgaW4gd2luZG93KSB7XG4gICAgICAgICAgICAgICAgd2luZG93LmNvb2tpZVN0b3JlLnJlbW92ZUV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIHRoaXMudXBkYXRlKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGVsc2Uge1xuICAgICAgICAgICAgICAgIHRoaXMuX3N0b3BQb2xsaW5nKCk7XG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICB9XG59XG5cbmV4cG9ydCB7IENvb2tpZXMgYXMgZGVmYXVsdCB9O1xuIl0sIm5hbWVzIjpbXSwiaWdub3JlTGlzdCI6WzBdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(ssr)/./node_modules/universal-cookie/esm/index.mjs\n");

/***/ })

};
;
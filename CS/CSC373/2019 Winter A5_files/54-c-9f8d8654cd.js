(window["canvasWebpackJsonp"]=window["canvasWebpackJsonp"]||[]).push([[54],{KVl8:function(t,e,n){(function(e){n=function(){"use strict"
var t=Array.isArray||function(t){return"[object Array]"==Object.prototype.toString.call(t)}
var n=y
var r=h
var i=c
var a=p
var o=m
var s=new RegExp(["(\\\\.)","([\\/.])?(?:(?:\\:(\\w+)(?:\\(((?:\\\\.|[^()])+)\\))?|\\(((?:\\\\.|[^()])+)\\))([+*?])?|(\\*))"].join("|"),"g")
function h(t){var e=[]
var n=0
var r=0
var i=""
var a
while(null!=(a=s.exec(t))){var o=a[0]
var h=a[1]
var c=a.index
i+=t.slice(r,c)
r=c+o.length
if(h){i+=h[1]
continue}if(i){e.push(i)
i=""}var p=a[2]
var f=a[3]
var l=a[4]
var d=a[5]
var v=a[6]
var g=a[7]
var w="+"===v||"*"===v
var m="?"===v||"*"===v
var y=p||"/"
var _=l||d||(g?".*":"[^"+y+"]+?")
e.push({name:f||n++,prefix:p||"",delimiter:y,optional:m,repeat:w,pattern:u(_)})}r<t.length&&(i+=t.substr(r))
i&&e.push(i)
return e}function c(t){return p(h(t))}function p(e){var n=new Array(e.length)
for(var r=0;r<e.length;r++)"object"===typeof e[r]&&(n[r]=new RegExp("^"+e[r].pattern+"$"))
return function(r){var i=""
var a=r||{}
for(var o=0;o<e.length;o++){var s=e[o]
if("string"===typeof s){i+=s
continue}var h=a[s.name]
var c
if(null==h){if(s.optional)continue
throw new TypeError('Expected "'+s.name+'" to be defined')}if(t(h)){if(!s.repeat)throw new TypeError('Expected "'+s.name+'" to not repeat, but received "'+h+'"')
if(0===h.length){if(s.optional)continue
throw new TypeError('Expected "'+s.name+'" to not be empty')}for(var p=0;p<h.length;p++){c=encodeURIComponent(h[p])
if(!n[o].test(c))throw new TypeError('Expected all "'+s.name+'" to match "'+s.pattern+'", but received "'+c+'"')
i+=(0===p?s.prefix:s.delimiter)+c}continue}c=encodeURIComponent(h)
if(!n[o].test(c))throw new TypeError('Expected "'+s.name+'" to match "'+s.pattern+'", but received "'+c+'"')
i+=s.prefix+c}return i}}function f(t){return t.replace(/([.+*?=^!:${}()[\]|\/])/g,"\\$1")}function u(t){return t.replace(/([=!:$\/()])/g,"\\$1")}function l(t,e){t.keys=e
return t}function d(t){return t.sensitive?"":"i"}function v(t,e){var n=t.source.match(/\((?!\?)/g)
if(n)for(var r=0;r<n.length;r++)e.push({name:r,prefix:null,delimiter:null,optional:false,repeat:false,pattern:null})
return l(t,e)}function g(t,e,n){var r=[]
for(var i=0;i<t.length;i++)r.push(y(t[i],e,n).source)
var a=new RegExp("(?:"+r.join("|")+")",d(n))
return l(a,e)}function w(t,e,n){var r=h(t)
var i=m(r,n)
for(var a=0;a<r.length;a++)"string"!==typeof r[a]&&e.push(r[a])
return l(i,e)}function m(t,e){e=e||{}
var n=e.strict
var r=false!==e.end
var i=""
var a=t[t.length-1]
var o="string"===typeof a&&/\/$/.test(a)
for(var s=0;s<t.length;s++){var h=t[s]
if("string"===typeof h)i+=f(h)
else{var c=f(h.prefix)
var p=h.pattern
h.repeat&&(p+="(?:"+c+p+")*")
p=h.optional?c?"(?:"+c+"("+p+"))?":"("+p+")?":c+"("+p+")"
i+=p}}n||(i=(o?i.slice(0,-2):i)+"(?:\\/(?=$))?")
i+=r?"$":n&&o?"":"(?=\\/|$)"
return new RegExp("^"+i,d(e))}function y(e,n,r){n=n||[]
if(t(n))r||(r={})
else{r=n
n=[]}if(e instanceof RegExp)return v(e,n,r)
if(t(e))return g(e,n,r)
return w(e,n,r)}n.parse=r
n.compile=i
n.tokensToFunction=a
n.tokensToRegExp=o
var _="undefined"!==typeof document
var b="undefined"!==typeof window
var x="undefined"!==typeof history
var E="undefined"!==typeof e
var k=_&&document.ontouchstart?"touchstart":"click"
var R=b&&!!(window.history.location||window.location)
function U(){this.callbacks=[]
this.exits=[]
this.current=""
this.len=0
this._decodeURLComponents=true
this._base=""
this._strict=false
this._running=false
this._hashbang=false
this.clickHandler=this.clickHandler.bind(this)
this._onpopstate=this._onpopstate.bind(this)}U.prototype.configure=function(t){var e=t||{}
this._window=e.window||b&&window
this._decodeURLComponents=false!==e.decodeURLComponents
this._popstate=false!==e.popstate&&b
this._click=false!==e.click&&_
this._hashbang=!!e.hashbang
var n=this._window
this._popstate?n.addEventListener("popstate",this._onpopstate,false):b&&n.removeEventListener("popstate",this._onpopstate,false)
this._click?n.document.addEventListener(k,this.clickHandler,false):_&&n.document.removeEventListener(k,this.clickHandler,false)
this._hashbang&&b&&!x?n.addEventListener("hashchange",this._onpopstate,false):b&&n.removeEventListener("hashchange",this._onpopstate,false)}
U.prototype.base=function(t){if(0===arguments.length)return this._base
this._base=t}
U.prototype._getBase=function(){var t=this._base
if(!!t)return t
var e=b&&this._window&&this._window.location
b&&this._hashbang&&e&&"file:"===e.protocol&&(t=e.pathname)
return t}
U.prototype.strict=function(t){if(0===arguments.length)return this._strict
this._strict=t}
U.prototype.start=function(t){var e=t||{}
this.configure(e)
if(false===e.dispatch)return
this._running=true
var n
if(R){var r=this._window
var i=r.location
n=this._hashbang&&~i.hash.indexOf("#!")?i.hash.substr(2)+i.search:this._hashbang?i.search+i.hash:i.pathname+i.search+i.hash}this.replace(n,null,true,e.dispatch)}
U.prototype.stop=function(){if(!this._running)return
this.current=""
this.len=0
this._running=false
var t=this._window
this._click&&t.document.removeEventListener(k,this.clickHandler,false)
b&&t.removeEventListener("popstate",this._onpopstate,false)
b&&t.removeEventListener("hashchange",this._onpopstate,false)}
U.prototype.show=function(t,e,n,r){var i=new P(t,e,this),a=this.prevContext
this.prevContext=i
this.current=i.path
false!==n&&this.dispatch(i,a)
false!==i.handled&&false!==r&&i.pushState()
return i}
U.prototype.back=function(t,e){var n=this
if(this.len>0){var r=this._window
x&&r.history.back()
this.len--}else t?setTimeout((function(){n.show(t,e)})):setTimeout((function(){n.show(n._getBase(),e)}))}
U.prototype.redirect=function(t,e){var n=this
"string"===typeof t&&"string"===typeof e&&C.call(this,t,(function(t){setTimeout((function(){n.replace(e)}),0)}))
"string"===typeof t&&"undefined"===typeof e&&setTimeout((function(){n.replace(t)}),0)}
U.prototype.replace=function(t,e,n,r){var i=new P(t,e,this),a=this.prevContext
this.prevContext=i
this.current=i.path
i.init=n
i.save()
false!==r&&this.dispatch(i,a)
return i}
U.prototype.dispatch=function(t,e){var n=0,r=0,i=this
function a(){var t=i.exits[r++]
if(!t)return o()
t(e,a)}function o(){var e=i.callbacks[n++]
if(t.path!==i.current){t.handled=false
return}if(!e)return O.call(i,t)
e(t,o)}e?a():o()}
U.prototype.exit=function(t,e){if("function"===typeof t)return this.exit("*",t)
var n=new T(t,null,this)
for(var r=1;r<arguments.length;++r)this.exits.push(n.middleware(arguments[r]))}
U.prototype.clickHandler=function(t){if(1!==this._which(t))return
if(t.metaKey||t.ctrlKey||t.shiftKey)return
if(t.defaultPrevented)return
var e=t.target
var n=t.path||(t.composedPath?t.composedPath():null)
if(n)for(var r=0;r<n.length;r++){if(!n[r].nodeName)continue
if("A"!==n[r].nodeName.toUpperCase())continue
if(!n[r].href)continue
e=n[r]
break}while(e&&"A"!==e.nodeName.toUpperCase())e=e.parentNode
if(!e||"A"!==e.nodeName.toUpperCase())return
var i="object"===typeof e.href&&"SVGAnimatedString"===e.href.constructor.name
if(e.hasAttribute("download")||"external"===e.getAttribute("rel"))return
var a=e.getAttribute("href")
if(!this._hashbang&&this._samePath(e)&&(e.hash||"#"===a))return
if(a&&a.indexOf("mailto:")>-1)return
if(i?e.target.baseVal:e.target)return
if(!i&&!this.sameOrigin(e.href))return
var o=i?e.href.baseVal:e.pathname+e.search+(e.hash||"")
o="/"!==o[0]?"/"+o:o
E&&o.match(/^\/[a-zA-Z]:\//)&&(o=o.replace(/^\/[a-zA-Z]:\//,"/"))
var s=o
var h=this._getBase()
0===o.indexOf(h)&&(o=o.substr(h.length))
this._hashbang&&(o=o.replace("#!",""))
if(h&&s===o&&(!R||"file:"!==this._window.location.protocol))return
t.preventDefault()
this.show(s)}
U.prototype._onpopstate=function(){var t=false
if(!b)return function(){}
_&&"complete"===document.readyState?t=true:window.addEventListener("load",(function(){setTimeout((function(){t=true}),0)}))
return function(e){if(!t)return
var n=this
if(e.state){var r=e.state.path
n.replace(r,e.state)}else if(R){var i=n._window.location
n.show(i.pathname+i.search+i.hash,void 0,void 0,false)}}}()
U.prototype._which=function(t){t=t||b&&this._window.event
return null==t.which?t.button:t.which}
U.prototype._toURL=function(t){var e=this._window
if("function"===typeof URL&&R)return new URL(t,e.location.toString())
if(_){var n=e.document.createElement("a")
n.href=t
return n}}
U.prototype.sameOrigin=function(t){if(!t||!R)return false
var e=this._toURL(t)
var n=this._window
var r=n.location
return r.protocol===e.protocol&&r.hostname===e.hostname&&(r.port===e.port||""===r.port&&80===e.port)}
U.prototype._samePath=function(t){if(!R)return false
var e=this._window
var n=e.location
return t.pathname===n.pathname&&t.search===n.search}
U.prototype._decodeURLEncodedURIComponent=function(t){if("string"!==typeof t)return t
return this._decodeURLComponents?decodeURIComponent(t.replace(/\+/g," ")):t}
function L(){var t=new U
function e(){return C.apply(t,arguments)}e.callbacks=t.callbacks
e.exits=t.exits
e.base=t.base.bind(t)
e.strict=t.strict.bind(t)
e.start=t.start.bind(t)
e.stop=t.stop.bind(t)
e.show=t.show.bind(t)
e.back=t.back.bind(t)
e.redirect=t.redirect.bind(t)
e.replace=t.replace.bind(t)
e.dispatch=t.dispatch.bind(t)
e.exit=t.exit.bind(t)
e.configure=t.configure.bind(t)
e.sameOrigin=t.sameOrigin.bind(t)
e.clickHandler=t.clickHandler.bind(t)
e.create=L
Object.defineProperty(e,"len",{get:function(){return t.len},set:function(e){t.len=e}})
Object.defineProperty(e,"current",{get:function(){return t.current},set:function(e){t.current=e}})
e.Context=P
e.Route=T
return e}function C(t,e){if("function"===typeof t)return C.call(this,"*",t)
if("function"===typeof e){var n=new T(t,null,this)
for(var r=1;r<arguments.length;++r)this.callbacks.push(n.middleware(arguments[r]))}else"string"===typeof t?this["string"===typeof e?"redirect":"show"](t,e):this.start(t)}function O(t){if(t.handled)return
var e
var n=this
var r=n._window
e=n._hashbang?R&&this._getBase()+r.location.hash.replace("#!",""):R&&r.location.pathname+r.location.search
if(e===t.canonicalPath)return
n.stop()
t.handled=false
R&&(r.location.href=t.canonicalPath)}function A(t){return t.replace(/([.+*?=^!:${}()[\]|/\\])/g,"\\$1")}function P(t,e,n){var r=this.page=n||C
var i=r._window
var a=r._hashbang
var o=r._getBase()
"/"===t[0]&&0!==t.indexOf(o)&&(t=o+(a?"#!":"")+t)
var s=t.indexOf("?")
this.canonicalPath=t
var h=new RegExp("^"+A(o))
this.path=t.replace(h,"")||"/"
a&&(this.path=this.path.replace("#!","")||"/")
this.title=_&&i.document.title
this.state=e||{}
this.state.path=t
this.querystring=~s?r._decodeURLEncodedURIComponent(t.slice(s+1)):""
this.pathname=r._decodeURLEncodedURIComponent(~s?t.slice(0,s):t)
this.params={}
this.hash=""
if(!a){if(!~this.path.indexOf("#"))return
var c=this.path.split("#")
this.path=this.pathname=c[0]
this.hash=r._decodeURLEncodedURIComponent(c[1])||""
this.querystring=this.querystring.split("#")[0]}}P.prototype.pushState=function(){var t=this.page
var e=t._window
var n=t._hashbang
t.len++
x&&e.history.pushState(this.state,this.title,n&&"/"!==this.path?"#!"+this.path:this.canonicalPath)}
P.prototype.save=function(){var t=this.page
x&&t._window.history.replaceState(this.state,this.title,t._hashbang&&"/"!==this.path?"#!"+this.path:this.canonicalPath)}
function T(t,e,r){this.page=r||$
var i=e||{}
i.strict=i.strict||r._strict
this.path="*"===t?"(.*)":t
this.method="GET"
this.regexp=n(this.path,this.keys=[],i)}T.prototype.middleware=function(t){var e=this
return function(n,r){if(e.match(n.path,n.params))return t(n,r)
r()}}
T.prototype.match=function(t,e){var n=this.keys,r=t.indexOf("?"),i=~r?t.slice(0,r):t,a=this.regexp.exec(decodeURIComponent(i))
if(!a)return false
delete e[0]
for(var o=1,s=a.length;o<s;++o){var h=n[o-1]
var c=this.page._decodeURLEncodedURIComponent(a[o])
void 0===c&&hasOwnProperty.call(e,h.name)||(e[h.name]=c)}return true}
var $=L()
var I=$
var S=$
I.default=S
return I},t.exports=n()
var n}).call(this,n("8oxB"))}}])

//# sourceMappingURL=54-c-9f8d8654cd.js.map
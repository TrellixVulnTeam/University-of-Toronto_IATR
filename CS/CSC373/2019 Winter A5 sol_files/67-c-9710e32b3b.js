(window["canvasWebpackJsonp"]=window["canvasWebpackJsonp"]||[]).push([[67,623,678],{"0crz":function(e,t,i){"use strict"
var a=i("ouhR")
var l=i.n(a)
var n=i("pQTu")
var _=i("m0r6")
Object(_["a"])(JSON.parse('{"ar":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"إظهار النص المقتبس","word_separator":" "}}},"cy":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"dangos testun wedi’i ddyfynnu","word_separator":" "}}},"da":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"vis tekst i gåseøjne","word_separator":" "}}},"da-x-k12":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"vis tekst i gåseøjne","word_separator":" "}}},"de":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"zitierten Text zeigen","word_separator":" "}}},"el":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"προβολή κειμένου που παρατίθεται"}}},"en-AU":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"show quoted text","word_separator":" "}}},"en-AU-x-unimelb":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"show quoted text","word_separator":" "}}},"en-CA":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"show quoted text","word_separator":" "}}},"en-GB":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"show quoted text","word_separator":" "}}},"en-GB-x-lbs":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"show quoted text","word_separator":" "}}},"en-GB-x-ukhe":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"show quoted text","word_separator":" "}}},"es":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"mostrar texto citado","word_separator":" "}}},"fa":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"نمایش متن نقل شده","word_separator":" "}}},"fi":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"näytä lainattu teksti","word_separator":" "}}},"fr":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"afficher le texte entre guillemets","word_separator":" "}}},"fr-CA":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"afficher le texte entre guillemets","word_separator":" "}}},"he":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"מציג ציטוט","word_separator":" "}}},"ht":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"afiche tèks site","word_separator":" "}}},"hu":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"idézett szöveg megjelenítése","word_separator":" "}}},"hy":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"ցույց տալ մեջբերվող տեքստը","word_separator":"-"}}},"is":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"Sýna ívitnaðan texta","word_separator":" "}}},"it":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"mostra testo citato","word_separator":" "}}},"ja":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"引用したテキストを表示","word_separator":" "}}},"ko":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"인용된 텍스트 표시","word_separator":" "}}},"mi":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"whakaatu kuputuhi faahiti","word_separator":"-"}}},"nb":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"vis den merkede teksten","word_separator":" "}}},"nb-x-k12":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"vis den merkede teksten","word_separator":" "}}},"nl":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"geciteerde tekst tonen","word_separator":" "}}},"nn":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"vis sitert tekst","word_separator":" "}}},"pl":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"pokaż cytowany fragment tekstu","word_separator":" "}}},"pt":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"exibir texto citado","word_separator":" "}}},"pt-BR":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"exibir texto citado","word_separator":" "}}},"ru":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"показать цитированный текст","word_separator":" "}}},"sl":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"prikaži citirano besedilo","word_separator":" "}}},"sv":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"visa citerad text","word_separator":" "}}},"sv-x-k12":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"visa citerad text","word_separator":" "}}},"tr":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"alıntılanan metni göster","word_separator":" "}}},"uk":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"Показати цитований текст","word_separator":" "}}},"zh-Hans":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"显示引用的文本","word_separator":" "}}},"zh-Hant":{"lib":{"text_helper":{"ellipsis":"...","quoted_text_toggle":"顯示引用的文字","word_separator":" "}}}}'))
i("jQeR")
i("0sPK")
var s=n["default"].scoped("lib.text_helper")
var o=i("5Ky4")
var r,c,u
r="LINK-PLACEHOLDER"
c=/\b((?:https?:\/\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}\/)(?:[^\s()<>]+|\([^\s()<>]*\))+(?:\([^\s()<>]*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))|(LINK-PLACEHOLDER)/gi
t["a"]=u={quoteClump:function(e){return"<div class='quoted_text_holder'> <a href='#' class='show_quoted_text_link'>"+Object(o["a"])(s.t("quoted_text_toggle","show quoted text"))+"</a> <div class='quoted_text' style='display: none;'> "+l.a.raw(e.join("\n"))+" </div> </div>"},formatMessage:function(e){var t,i,a,l,n,_,s,d
l=[]
n=[]
e=e.replace(c,(function(e,t){var i
n.push(e===r?r:(i=e,"http://"===i.slice(0,7)||"https://"===i.slice(0,8)||(i="http://"+i),l.push(i),"<a href='"+Object(o["a"])(i)+"'>"+Object(o["a"])(e)+"</a>"))
return r}))
e=Object(o["a"])(e)
e=e.replace(new RegExp(r,"g"),(function(e,t){return n.shift()}))
e=e.replace(/\n/g,"<br />\n")
_=[]
s=[]
d=e.split("\n")
for(t=0,i=d.length;t<i;t++){a=d[t]
if(a.match(/^(&gt;|>)/))s.push(a)
else{s.length&&_.push(u.quoteClump(s))
s=[]
_.push(a)}}s.length&&_.push(u.quoteClump(s))
return _.join("\n")},delimit:function(e){var t,i,a,l,n
if(isNaN(e))return String(e)
n=e<0?"-":""
t=Math.abs(e)
if(Infinity===t)return String(e)
i=Math.floor(t)
l=t===i?"":String(t).replace(/^\d+\./,".")
while(i>=1e3){a=String(i).replace(/\d+(\d\d\d)$/,",$1")
i=Math.floor(i/1e3)
l=a+l}return n+String(i)+l},truncateText:function(e,t){var i,a,l,n,_,o
null==t&&(t={})
a=null!=(n=t.max)?n:30
i=s.t("ellipsis","...")
o=s.t("word_separator"," ")
e=(null!=e?e:"").replace(/\s+/g,o).trim()
if(!e||e.length<=a)return e
_=0
while(true){l=e.indexOf(o,_+1)
if(l<0||l>a-i.length)break
_=l}_||(_=a-i.length)
return e.substring(0,_)+i},plainText:function(e){return e.replace(/(<([^>]+)>)/gi,"")}}},B1vq:function(e,t,i){"use strict"
var a=i("ouhR")
var l=i.n(a)
i("s/PJ")
l.a.fn.scrollToVisible=function(e){const t={}
const i=l()(e)
if(0===i.length)return
let a=i.offset(),n=i.outerWidth(),_=i.outerHeight(),s=a.top,o=s+_,r=a.left,c=r+n,u="html,body"==this.selector?l.a.windowScrollTop():this.scrollTop(),d=this.scrollLeft(),f=this.outerHeight(),m=this.outerWidth()
if("html,body"!=this.selector){let e=l()("body").offset()
this.each((function(){try{e=l()(this).offset()
return false}catch(e){}}))
s-=e.top
o-=e.top
r-=e.left
c-=e.left}if("HTML"==this[0].tagName||"BODY"==this[0].tagName){f=l()(window).height()
l()("#wizard_box:visible").length>0&&(f-=l()("#wizard_box:visible").height())
m=l()(window).width()
s-=u
r-=d
o-=u
c-=d}s<0||f<_&&o>f?t.scrollTop=s+u:o>f&&(t.scrollTop=o+u-f+20)
r<0?t.scrollLeft=r+d:c>m&&(t.scrollLeft=c+d-m+20)
1==t.scrollTop&&(t.scrollTop=0)
1==t.scrollLeft&&(t.scrollLeft=0)
this.scrollTop(t.scrollTop)
this.scrollLeft(t.scrollLeft)
return this}},BHWx:function(e,t,i){"use strict"
i.r(t)
var a=i("ODXe")
var l=i("mNVu")
var n=i("Cf7h")
const _=ENV.FILES_CONTEXTS||[]
const s={contexts:_,contextsDictionary:_.reduce((e,t)=>{const i=Array.from(Object(n["a"])(t.asset_string)),l=Object(a["a"])(i,2),_=l[0],s=l[1]
t.contextType=_
t.contextId=s
e[[_,s].join("_")]=t
return e},{}),showingAllContexts:window.location.pathname.match(/^\/files/),contextType:null!=_[0]?_[0].contextType:void 0,contextId:null!=_[0]?_[0].contextId:void 0,rootFolders:_.map(e=>{if(ENV.current_user_id){const t=new l["a"]({custom_name:e.name,context_type:e.contextType.replace(/s$/,""),context_id:e.contextId})
t.url="/api/v1/".concat(e.contextType,"/").concat(e.contextId,"/folders/root")
t.fetch()
return t}})}
s.contextFor=function(e){let t
e.collection&&e.collection.parentFolder&&(e=e.collection.parentFolder)
if(e instanceof l["a"]){const i=e
t="".concat(i&&i.get("context_type"),"s_").concat(i&&i.get("context_id")).toLowerCase()}else e.contextType&&e.contextId&&(t="".concat(e.contextType,"_").concat(e.contextId).toLowerCase())
return s.contextsDictionary&&s.contextsDictionary[t]}
s.userHasPermission=function(e,t){if(!e)return false
return s.contextFor(e)&&s.contextFor(e).permissions&&s.contextFor(e).permissions[t]}
s.baseUrl=s.showingAllContexts?"/files":"/".concat(s.contextType,"/").concat(s.contextId,"/files")
t["default"]=s},"Ewk/":function(e,t,i){"use strict"
var a=i("An8g")
var l=i("q1tI")
var n=i.n(l)
var _=i("fhzG")
var s=i.n(_)
var o=i("i8i4")
var r=i.n(o)
var c=i("ouhR")
var u=i.n(c)
var d=i("pQTu")
var f=i("m0r6")
Object(f["a"])(JSON.parse('{"ar":{"editing_permissions_for_name_3503e235":"أذونات التحرير لصالح: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} غير ظاهر في ملفات الطالب - انقر للتعديل","filename_is_published_click_to_modify_38a4a269":"%{fileName} منشور - انقر للتعديل","filename_is_restricted_9aaf9250":"%{fileName} - %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName}  %{restricted} - انقر للتعديل","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} غير منشور - انقر للتعديل","not_visible_in_student_files_22f11883":"غير مرئي في ملفات الطالب","published_4bb5209e":"تم النشر","this_file_9443cda1":"هذا الملف","unpublished_8b6107d6":"غير منشور"},"cy":{"editing_permissions_for_name_3503e235":"Golygu hawliau ar gyfer: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"Dydy %{fileName} ddim yn ymddangos mewn ffeiliau myfyrwyr – Cliciwch i addasu hyn","filename_is_published_click_to_modify_38a4a269":"%{fileName} wedi Cyhoeddi - Cliciwch i addasu","filename_is_restricted_9aaf9250":"%{fileName} yn %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} %{restricted} - Cliciwch i addasu","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} heb Gyhoeddi - Cliciwch i addasu","not_visible_in_student_files_22f11883":"Ddim yn ymddangos mewn ffeiliau myfyrwyr","published_4bb5209e":"Wedi cyhoeddi","this_file_9443cda1":"Mae’r ffeil hon","unpublished_8b6107d6":"Heb gyhoeddi"},"da":{"editing_permissions_for_name_3503e235":"Redigerer tilladelser til: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikke synligt i filer for studerende - Klik for at ændre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er offentliggjort, klik for at ændre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted}, klik for at ændre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er ikke offentliggjort, klik for at ændre","not_visible_in_student_files_22f11883":"Ikke synlig i filer for studerende","published_4bb5209e":"Offentliggjort","this_file_9443cda1":"Denne fil","unpublished_8b6107d6":"Ikke offentliggjort"},"da-x-k12":{"editing_permissions_for_name_3503e235":"Redigerer tilladelser til: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikke synligt i filer for elever - Klik for at ændre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er offentliggjort, klik for at ændre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted}, klik for at ændre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er ikke offentliggjort, klik for at ændre","not_visible_in_student_files_22f11883":"Ikke synlig i filer for elever","published_4bb5209e":"Offentliggjort","this_file_9443cda1":"Denne fil","unpublished_8b6107d6":"Ikke offentliggjort"},"de":{"editing_permissions_for_name_3503e235":"Änderungsberechtigungen für: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} ist in Studentendateien nicht sichtbar – Um das zu ändern, hier klicken","filename_is_published_click_to_modify_38a4a269":"%{fileName} ist veröffentlicht – zum Ändern anklicken","filename_is_restricted_9aaf9250":"%{fileName} ist %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Ist %{restricted} – zum Ändern klicken","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Ist nicht veröffentlicht – zum Ändern anklicken","not_visible_in_student_files_22f11883":"In Studentendateien nicht sichtbar.","published_4bb5209e":"Veröffentlicht","this_file_9443cda1":"Diese Datei","unpublished_8b6107d6":"Nicht veröffentlicht"},"el":{"editing_permissions_for_name_3503e235":"\\u003cmrk mid=\\"7571\\" mtype=\\"seg\\"\\u003eΆδειες επεξεργασίας για:\\u003c/mrk\\u003e \\u003cmrk mid=\\"7572\\" mtype=\\"seg\\"\\u003e%{name}\\u003c/mrk\\u003e","published_4bb5209e":"Δημοσιευμένο/α","this_file_9443cda1":"Αυτό το αρχείο","unpublished_8b6107d6":"Μη δημοσιευμένο"},"en-AU":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-AU-x-unimelb":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-CA":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-GB":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-GB-x-lbs":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-GB-x-ukhe":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"es":{"editing_permissions_for_name_3503e235":"Editando permisos para lo siguiente: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} no es visible en los archivos de los estudiantes. Haga clic para modificar","filename_is_published_click_to_modify_38a4a269":"%{fileName} está publicado: Haga clic para modificar","filename_is_restricted_9aaf9250":"%{fileName} es %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} está %{restricted} - Haga clic para modificar","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} no está publicado: Haga clic para modificar","not_visible_in_student_files_22f11883":"No visible en los archivos de los estudiantes","published_4bb5209e":"Publicado","this_file_9443cda1":"Este archivo","unpublished_8b6107d6":"No publicado"},"fa":{"editing_permissions_for_name_3503e235":"مجوزهای ویرایش برای: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} منتشر شده است. برای تغییر کلیک کنید","filename_is_restricted_9aaf9250":"%{fileName} %{restricted} است","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} %{restricted}است- برای تغییر کلیک کنید","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} منتشر نشده است. برای تغییر کلیک کنید","published_4bb5209e":"منتشر شده","this_file_9443cda1":"این فایل","unpublished_8b6107d6":"منتشر نشده"},"fi":{"editing_permissions_for_name_3503e235":"Muokataan käyttöoikeuksia kohteelle: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} ei ole näkyvissä opiskelijatiedostoille - Muokkaa napsauttamalla","filename_is_published_click_to_modify_38a4a269":"%{fileName} On julkaistu - Napsauta muokataksesi","filename_is_restricted_9aaf9250":"%{fileName} on %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} on %{restricted} - Napsauta muokkaa","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Julkaisu on kumottu - Napsauta muokataksesi","not_visible_in_student_files_22f11883":"Ei näkyvillä opiskelijan tiedostoissa","published_4bb5209e":"Julkaistu","this_file_9443cda1":"Tämä tiedosto","unpublished_8b6107d6":"Julkaisematon"},"fr":{"editing_permissions_for_name_3503e235":"Modifier les autorisations de : %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} N’est pas visible parmi les fichiers des élèves - Cliquez pour modifier.","filename_is_published_click_to_modify_38a4a269":"%{fileName} est publié – Cliquez pour modifier","filename_is_restricted_9aaf9250":"%{fileName} est %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} est %{restricted} – Cliquez pour modifier","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} n’est pas publié – Cliquez pour modifier","not_visible_in_student_files_22f11883":"Non visible dans les fichiers des élèves","published_4bb5209e":"Publié","this_file_9443cda1":"Ce fichier","unpublished_8b6107d6":"Non publié(e)(s)"},"fr-CA":{"editing_permissions_for_name_3503e235":"Modifier les autorisations de : %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} est non visible dans les fichiers des étudiants - Cliquez pour modifier","filename_is_published_click_to_modify_38a4a269":"%{fileName} Est publié - Cliquez pour modifier","filename_is_restricted_9aaf9250":"%{fileName} est %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Est %{restricted} - Cliquez pour modifier","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Est non publié - Cliquez pour modifier","not_visible_in_student_files_22f11883":"Non visible dans les fichiers de l’étudiant","published_4bb5209e":"Date de publication","this_file_9443cda1":"Ce fichier","unpublished_8b6107d6":"Non publié"},"he":{"editing_permissions_for_name_3503e235":"עריכת הרשאות ל: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} פורסם. - הקש/י כדי לעדכן","filename_is_restricted_9aaf9250":"%{fileName} הנו%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} הנו %{restricted} - הקש/י כדי לעדכן","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} טרם פורסם - הקש/י כדי לעדכן","published_4bb5209e":"פורסם","this_file_9443cda1":"קובץ זה","unpublished_8b6107d6":"לא פורסם"},"ht":{"editing_permissions_for_name_3503e235":"Modifikasyon pèmisyon pou: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} pa vizib nan fichye elèv yo - Klike pou ka chanje","filename_is_published_click_to_modify_38a4a269":"%{fileName} Pibliye - Klike pou modifye","filename_is_restricted_9aaf9250":"%{fileName} se %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} se %{restricted} - Klike pou modifye","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Pa pibliye - Klike pou modifye","not_visible_in_student_files_22f11883":"Pa vizib nan fichye elèv yo","published_4bb5209e":"Pibliye","this_file_9443cda1":"Fichye sa a","unpublished_8b6107d6":"Pa Pibliye"},"hu":{"editing_permissions_for_name_3503e235":"%{name} jogainak szerkesztése","published_4bb5209e":"Publikált","this_file_9443cda1":"Ez a fájl","unpublished_8b6107d6":"Nem publikált"},"hy":{"editing_permissions_for_name_3503e235":"Խմբագրման թույլտվություն %{name}-ի համար","published_4bb5209e":"Հրապարակված","this_file_9443cda1":"Այս ֆայլը","unpublished_8b6107d6":"Չհրապարակված"},"is":{"editing_permissions_for_name_3503e235":"Breyta heimildum fyrir: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ekki sýnilegt í skrám nemanda - smelltu til að breyta","filename_is_published_click_to_modify_38a4a269":"%{fileName} er birt - Smelltu til að breyta","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - Smelltu til að breyta","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er óbirt - Smelltu til að breyta","not_visible_in_student_files_22f11883":"Ekki sýnilegt í skrám nemanda","published_4bb5209e":"Birt","this_file_9443cda1":"Þessi skrá","unpublished_8b6107d6":"Óbirt"},"it":{"editing_permissions_for_name_3503e235":"Modifica autorizzazioni per: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} non è visibile nei file studente - Fare clic per modificare","filename_is_published_click_to_modify_38a4a269":"%{fileName} è pubblicato - Fai clic per modificare","filename_is_restricted_9aaf9250":"%{fileName} è %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} è %{restricted} - Fai clic per modificare","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} non è pubblicato - Fai clic per modificare","not_visible_in_student_files_22f11883":"Non visibile nei file degli studenti","published_4bb5209e":"Pubblicato","this_file_9443cda1":"Questo file","unpublished_8b6107d6":"Non pubblicato"},"ja":{"editing_permissions_for_name_3503e235":"編集権限: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName}は、受講生のファイルには表示されません - クリックして変更します","filename_is_published_click_to_modify_38a4a269":"%{fileName} 公開されています - クリックして修正する","filename_is_restricted_9aaf9250":"%{fileName} は%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} %{restricted} - クリックして変更","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} 非公開となっています - クリックして変更","not_visible_in_student_files_22f11883":"受講生ファイルでは表示できません。","published_4bb5209e":"公開済み","this_file_9443cda1":"このファイル","unpublished_8b6107d6":"未公開"},"mi":{"editing_permissions_for_name_3503e235":"Whakatika whakāetanga mō: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} kaore e kitea i roto i ngā ākonga kōnae Pāwhiri ki te whakamahi","filename_is_published_click_to_modify_38a4a269":"%{fileName} Kei te whakaputaina - Pāwhiritia ki te whakarerekē","filename_is_restricted_9aaf9250":"%{fileName} ko %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Ko %{restricted} Pāwhiritia ki te whakarerekē","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Kua kore e whakaputaina - Pāwhiritia ki te whakarerekē","not_visible_in_student_files_22f11883":"Kaore i kites i roto i ngā ākonga kōnae","published_4bb5209e":"I whakaputaina","this_file_9443cda1":"tēnei kōnae","unpublished_8b6107d6":"Kaore i"},"nb":{"editing_permissions_for_name_3503e235":"Redigerer rettigheter for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikke synlig i studentfiler - klikk for å endre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er publisert - Klikk for å endre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - Klikk for å endre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er upublisert - Klikk for å endre","not_visible_in_student_files_22f11883":"Ikke synlig i studentfiler","published_4bb5209e":"Publisert","this_file_9443cda1":"denne filen","unpublished_8b6107d6":"Ikke publisert"},"nb-x-k12":{"editing_permissions_for_name_3503e235":"Redigerer rettigheter for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikke synlig i elevfiler - klikk for å endre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er publisert - Klikk for å endre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - Klikk for å endre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er upublisert - Klikk for å endre","not_visible_in_student_files_22f11883":"Ikke synlig i elevfiler","published_4bb5209e":"Publisert","this_file_9443cda1":"denne filen","unpublished_8b6107d6":"Ikke publisert"},"nl":{"editing_permissions_for_name_3503e235":"Vergunningen bewerken voor: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is niet zichtbaar in cursistbestanden - Klik om te wijzigen","filename_is_published_click_to_modify_38a4a269":"%{fileName} is gepubliceerd - Klik om te wijzigen","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Klik om te wijzigen","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is niet gepubliceerd - Klik om te wijzigen","not_visible_in_student_files_22f11883":"Niet zichtbaar in cursistbestanden.","published_4bb5209e":"Gepubliceerd","this_file_9443cda1":"Dit bestand","unpublished_8b6107d6":"Niet-gepubliceerd"},"nn":{"editing_permissions_for_name_3503e235":"Rediger løyve for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikkje synleg i studentfiler - klikk for å endre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er publisert - klikk for å endre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - klikk for å endre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er upublisert - klikk for å endre","not_visible_in_student_files_22f11883":"Ikkje synleg i studentfiler","published_4bb5209e":"Publisert","this_file_9443cda1":"Denne fila","unpublished_8b6107d6":"Ikkje publisert"},"pl":{"editing_permissions_for_name_3503e235":"Uprawnienia do edycji posiada: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} nie jest widoczna w plikach uczestnikach – Kliknij, aby zmienić","filename_is_published_click_to_modify_38a4a269":"%{fileName} jest opublikowany – kliknij, aby zmienić.","filename_is_restricted_9aaf9250":"%{fileName} jest %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} jest %{restricted} – kliknij, aby zmienić.","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} jest nieopublikowany – kliknij, aby zmienić.","not_visible_in_student_files_22f11883":"Niewidoczne w plikach uczestników","published_4bb5209e":"Opublikowane","this_file_9443cda1":"Ten plik","unpublished_8b6107d6":"Nieopublikowane"},"pt":{"editing_permissions_for_name_3503e235":"Permissões de edição para: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} não está visível nos ficheiros dos alunos - Clique para modificar","filename_is_published_click_to_modify_38a4a269":"%{fileName} Está publicado - Clique para modificar","filename_is_restricted_9aaf9250":"%{fileName} Está %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Está %{restricted} - Clique para modificar","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Não está publicado - Clique para modificar","not_visible_in_student_files_22f11883":"Não visível nos ficheiros dos alunos","published_4bb5209e":"Publicado","this_file_9443cda1":"Este ficheiro","unpublished_8b6107d6":"Não publicado"},"pt-BR":{"editing_permissions_for_name_3503e235":"Permissões de edição para: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} Não está visível nos arquivos do aluno - Clique para modificar","filename_is_published_click_to_modify_38a4a269":"%{fileName} está publicado - Clique para modificar","filename_is_restricted_9aaf9250":"%{fileName} é %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} está %{restricted} - Clique para modificar","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} não está publicado - Clique para modificar","not_visible_in_student_files_22f11883":"Invisível nos arquivos de alunos","published_4bb5209e":"Publicado","this_file_9443cda1":"Este arquivo","unpublished_8b6107d6":"Não publicado"},"ru":{"editing_permissions_for_name_3503e235":"Редактирование разрешений для: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} не отображается в файлах учащихся - нажмите для изменения","filename_is_published_click_to_modify_38a4a269":"%{fileName} Опубликован - Нажмите для изменения","filename_is_restricted_9aaf9250":"%{fileName} является %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} является %{restricted} - Нажмите для изменения","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Не опубликован - Нажмите для изменения","not_visible_in_student_files_22f11883":"Не отображается в файлах учащихся","published_4bb5209e":"Опубликовано","this_file_9443cda1":"Этот файл","unpublished_8b6107d6":"Не опубликовано"},"sl":{"editing_permissions_for_name_3503e235":"Urejanje dovoljenj za: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} je objavljeno – kliknite, da prilagodite.","filename_is_restricted_9aaf9250":"%{fileName} je %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} je %{restricted} – kliknite, da prilagodite.","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} je neobjavljeno – kliknite, da prilagodite.","published_4bb5209e":"Objavljeno","this_file_9443cda1":"Ta datoteka","unpublished_8b6107d6":"Neobjavljeno"},"sv":{"editing_permissions_for_name_3503e235":"Redigerar tillstånd för %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} är inte synlig i studentfiler – Klicka för att ändra","filename_is_published_click_to_modify_38a4a269":"%{fileName} är publicerad - klicka för att modifiera","filename_is_restricted_9aaf9250":"%{fileName} är %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} är %{restricted} - klicka för att modifiera","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Är opublicerad - klicka för att modifiera","not_visible_in_student_files_22f11883":"Ej synlig i studentfiler","published_4bb5209e":"Publicerad","this_file_9443cda1":"Denna filen","unpublished_8b6107d6":"Avpublicerad"},"sv-x-k12":{"editing_permissions_for_name_3503e235":"Redigerar tillstånd för %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} är publicerad - klicka för att modifiera","filename_is_restricted_9aaf9250":"%{fileName} är %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} är %{restricted} - klicka för att modifiera","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Är opublicerad - klicka för att modifiera","published_4bb5209e":"Publicerad","this_file_9443cda1":"Denna filen","unpublished_8b6107d6":"Avpublicerad"},"tr":{"editing_permissions_for_name_3503e235":"%{name} için izinler düzenleniyor","filename_is_restricted_9aaf9250":"%{fileName}  %{restricted}dir","published_4bb5209e":"Yayınlandı","this_file_9443cda1":"Bu dosya","unpublished_8b6107d6":"Yayınlanmamış"},"uk":{"editing_permissions_for_name_3503e235":"Редагування дозволів для: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} опубліковано - Натисніть, щоб змінити","filename_is_restricted_9aaf9250":"%{fileName} є %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} є %{restricted} - Натисніть, щоб змінити","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} неопубліковано - Натисніть, щоб змінити","published_4bb5209e":"Опубліковано","this_file_9443cda1":"Цей файл","unpublished_8b6107d6":"Публікацію відмінено"},"zh-Hans":{"editing_permissions_for_name_3503e235":"为%{name}的编辑权限","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName}在学生文件中不显示 - 请点击调整","filename_is_published_click_to_modify_38a4a269":"%{fileName} 已发布 - 单击以修改","filename_is_restricted_9aaf9250":"%{fileName} 是%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} 是 %{restricted} - 单击以修改","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} 未发布 - 单击以修改","not_visible_in_student_files_22f11883":"在学生文件中不可见","published_4bb5209e":"已发布","this_file_9443cda1":"此文件","unpublished_8b6107d6":"取消发布"},"zh-Hant":{"editing_permissions_for_name_3503e235":"編輯權限：%{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} 在學生檔案中無法看到 - 按一下以修改","filename_is_published_click_to_modify_38a4a269":"%{fileName} 已發佈 - 按一下進行修改","filename_is_restricted_9aaf9250":"%{fileName} 是%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} 已 %{restricted} - 按一下進行修改","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} 未發佈 - 按一下進行修改","not_visible_in_student_files_22f11883":"在學生檔案中看不到","published_4bb5209e":"已發佈","this_file_9443cda1":"此文儅","unpublished_8b6107d6":"已取消發佈"}}'))
i("jQeR")
i("0sPK")
var m=d["default"].scoped("publish_cloud")
var b=i("17x9")
var p=i.n(b)
Object(f["a"])(JSON.parse('{"ar":{"available_after_unlock_at_b5682224":"متاح بعد %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"متاح بعد %{unlock_at} حتى %{lock_at}","available_until_lock_at_ab022445":"متاح حتى %{lock_at}"},"cy":{"available_after_unlock_at_b5682224":"Ar gael ar ôl %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Ar gael ar ôl %{unlock_at} tan %{lock_at}","available_until_lock_at_ab022445":"Ar gael tan %{lock_at}"},"da":{"available_after_unlock_at_b5682224":"Tilgængelig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgængelig efter %{unlock_at} indtil %{lock_at}","available_until_lock_at_ab022445":"Tilgængelig til %{lock_at}"},"da-x-k12":{"available_after_unlock_at_b5682224":"Tilgængelig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgængelig efter %{unlock_at} indtil %{lock_at}","available_until_lock_at_ab022445":"Tilgængelig til %{lock_at}"},"de":{"available_after_unlock_at_b5682224":"Verfügbar von %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Verfügbar von %{unlock_at} bis %{lock_at}","available_until_lock_at_ab022445":"Verfügbar bis %{lock_at}"},"el":{"available_after_unlock_at_b5682224":"Διαθέσιμο μετά από τις %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Διαθέσιμο από τις %{unlock_at} έως τις %{lock_at}","available_until_lock_at_ab022445":"Διαθέσιμο έως τις %{lock_at}"},"en-AU":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-AU-x-unimelb":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-CA":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-GB":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-GB-x-lbs":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-GB-x-ukhe":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"es":{"available_after_unlock_at_b5682224":"Disponible a partir de %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponible a partir de %{unlock_at} hasta %{lock_at}","available_until_lock_at_ab022445":"Disponible hasta %{lock_at}"},"fa":{"available_after_unlock_at_b5682224":"بعد از %{unlock_at} در دسترس است","available_after_unlock_at_until_lock_at_499e8092":"بعد از %{unlock_at} تا %{lock_at} در دسترس است","available_until_lock_at_ab022445":"تا %{lock_at} قابل دسترسی است"},"fi":{"available_after_unlock_at_b5682224":"Saatavilla %{unlock_at} jälkeen","available_after_unlock_at_until_lock_at_499e8092":"Saatavissa %{unlock_at} jälkeen %{lock_at} asti","available_until_lock_at_ab022445":"Saatavissa asti %{lock_at}"},"fr":{"available_after_unlock_at_b5682224":"Disponible après %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponible après %{unlock_at} et jusqu’à %{lock_at}","available_until_lock_at_ab022445":"Disponible jusqu’à %{lock_at}"},"fr-CA":{"available_after_unlock_at_b5682224":"Disponible après %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponible après %{unlock_at} et jusqu’à %{lock_at}","available_until_lock_at_ab022445":"Disponible jusqu’à %{lock_at}"},"he":{"available_after_unlock_at_b5682224":"זמין אחרי %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"זמין אחרי %{unlock_at}  עד %{lock_at}","available_until_lock_at_ab022445":"זמין עד %{lock_at}"},"ht":{"available_after_unlock_at_b5682224":"Disponib aprè %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponib aprè %{unlock_at} jiska %{lock_at}","available_until_lock_at_ab022445":"Disponib jiska %{lock_at}"},"hu":{"available_after_unlock_at_b5682224":"Elérhető ettől %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Elérhető ettől %{unlock_at}, eddig: %{lock_at}","available_until_lock_at_ab022445":"Elérhető eddig: %{lock_at}"},"hy":{"available_after_unlock_at_b5682224":"Հասանելի է %{unlock_at}-ից հետո","available_after_unlock_at_until_lock_at_499e8092":"Հասանելի է %{unlock_at}-ից հետո մինչև %{lock_at}","available_until_lock_at_ab022445":"Հասանելի է մինչև %{lock_at}"},"is":{"available_after_unlock_at_b5682224":"Tiltækt eftir %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tiltækt eftir %{unlock_at} til %{lock_at}","available_until_lock_at_ab022445":"Tiltækt til %{lock_at}"},"it":{"available_after_unlock_at_b5682224":"Disponibile dopo %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponibile dopo %{unlock_at} fino a %{lock_at}","available_until_lock_at_ab022445":"Disponibile fino a %{lock_at}"},"ja":{"available_after_unlock_at_b5682224":"%{unlock_at} 後に利用可能","available_after_unlock_at_until_lock_at_499e8092":"%{unlock_at} 後に %{lock_at} まで利用可能","available_until_lock_at_ab022445":"%{lock_at} まで利用可能"},"mi":{"available_after_unlock_at_b5682224":"Wātea i muri %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Wātea i muri %{unlock_at} noa %{lock_at}","available_until_lock_at_ab022445":"Wātea noa %{lock_at}"},"nb":{"available_after_unlock_at_b5682224":"Tilgjengelig etter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgjengelig etter %{unlock_at} inntil %{lock_at}","available_until_lock_at_ab022445":"Tilgjengelig til %{lock_at}"},"nb-x-k12":{"available_after_unlock_at_b5682224":"Tilgjengelig etter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgjengelig etter %{unlock_at} inntil %{lock_at}","available_until_lock_at_ab022445":"Tilgjengelig til %{lock_at}"},"nl":{"available_after_unlock_at_b5682224":"Beschikbaar na %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Beschikbaar na %{unlock_at} en tot en met %{lock_at}","available_until_lock_at_ab022445":"Beschikbaar tot %{lock_at}"},"nn":{"available_after_unlock_at_b5682224":"Tilgjengeleg etter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgjengeleg etter %{unlock_at} til %{lock_at}","available_until_lock_at_ab022445":"Tilgjengeleg til %{lock_at}"},"pl":{"available_after_unlock_at_b5682224":"Dostępne po %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Dostępne po %{unlock_at} aż do %{lock_at}","available_until_lock_at_ab022445":"Dostępne do %{lock_at}"},"pt":{"available_after_unlock_at_b5682224":"Disponível após %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponível após %{unlock_at} até %{lock_at}","available_until_lock_at_ab022445":"Disponível até %{lock_at}"},"pt-BR":{"available_after_unlock_at_b5682224":"Disponível após %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponível após %{unlock_at} até %{lock_at}","available_until_lock_at_ab022445":"Disponível até %{lock_at}"},"ru":{"available_after_unlock_at_b5682224":"Доступно с %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Доступно с %{unlock_at} до %{lock_at}","available_until_lock_at_ab022445":"Доступно до %{lock_at}"},"sl":{"available_after_unlock_at_b5682224":"Na voljo po %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Na voljo po %{unlock_at} do %{lock_at}","available_until_lock_at_ab022445":"Na voljo do %{lock_at}"},"sv":{"available_after_unlock_at_b5682224":"Tillgänglig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tillgänglig efter %{unlock_at} till %{lock_at}","available_until_lock_at_ab022445":"Tillgänglig tills %{lock_at}"},"sv-x-k12":{"available_after_unlock_at_b5682224":"Tillgänglig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tillgänglig efter %{unlock_at} till %{lock_at}","available_until_lock_at_ab022445":"Tillgänglig tills %{lock_at}"},"tr":{"available_after_unlock_at_b5682224":"%{unlock_at} tarihinden sonra geçerli","available_after_unlock_at_until_lock_at_499e8092":"%{unlock_at} tarihinden sonra %{lock_at} tarihine kadar geçerli","available_until_lock_at_ab022445":"%{lock_at} tarihine kadar geçerli"},"uk":{"available_after_unlock_at_b5682224":"Доступно після %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Доступно після %{unlock_at} до %{lock_at}","available_until_lock_at_ab022445":"Доступно до %{lock_at}"},"zh-Hans":{"available_after_unlock_at_b5682224":"%{unlock_at} 之后可用","available_after_unlock_at_until_lock_at_499e8092":"%{unlock_at} 之后、%{lock_at} 之前可用","available_until_lock_at_ab022445":"%{lock_at} 之前可用"},"zh-Hant":{"available_after_unlock_at_b5682224":"在 %{unlock_at} 之後可用","available_after_unlock_at_until_lock_at_499e8092":"在 %{unlock_at} 之後和 %{lock_at} 之前可用","available_until_lock_at_ab022445":"可用截止時間 %{lock_at}"}}'))
var h=d["default"].scoped("broccoli_cloud")
var k=i("lUQV")
i("MWZS")
i("UlQx")
var g={displayName:"PublishCloud",propTypes:{togglePublishClassOn:p.a.object,model:k["a"].filesystemObject,userCanManageFilesForContext:p.a.bool.isRequired,fileName:p.a.string},getInitialState(){return this.extractStateFromModel(this.props.model)},componentDidMount(){this.props.togglePublishClassOn&&this.updatePublishClassElements()},componentDidUpdate(){this.props.togglePublishClassOn&&this.updatePublishClassElements()},componentWillMount(){const e=e=>this.setState(this.extractStateFromModel(e))
this.props.model.on("change",e,this)},componentWillUnmount(){this.props.model.off(null,null,this)},updatePublishClassElements(){return this.props.togglePublishClassOn.classList[this.state.published?"add":"remove"]("ig-published")},getRestrictedText(){if(this.props.model.get("unlock_at")&&this.props.model.get("lock_at"))return h.t("Available after %{unlock_at} until %{lock_at}",{unlock_at:u.a.datetimeString(this.props.model.get("unlock_at")),lock_at:u.a.datetimeString(this.props.model.get("lock_at"))})
if(this.props.model.get("unlock_at")&&!this.props.model.get("lock_at"))return h.t("Available after %{unlock_at}",{unlock_at:u.a.datetimeString(this.props.model.get("unlock_at"))})
if(!this.props.model.get("unlock_at")&&this.props.model.get("lock_at"))return h.t("Available until %{lock_at}",{lock_at:u.a.datetimeString(this.props.model.get("lock_at"))})},extractStateFromModel:e=>({published:!e.get("locked"),restricted:!!e.get("lock_at")||!!e.get("unlock_at"),hidden:!!e.get("hidden")}),togglePublishedState(){this.setState({published:!this.state.published,restricted:false,hidden:false})}}
i("YGE8")
g.openRestrictedDialog=function(){const e=u()("<div>").dialog({title:m.t("Editing permissions for: %{name}",{name:this.props.model.displayName()}),width:800,minHeight:300,close(){r.a.unmountComponentAtNode(this)
u()(this).remove()}})
i.e(121).then(i.bind(null,"Vm4Q")).then(t=>{let i=t.default
r.a.render(Object(a["a"])(i,{usageRightsRequiredForContext:this.props.usageRightsRequiredForContext,models:[this.props.model],closeDialog:()=>{e.dialog("close")}}),e[0])})}
var v=Object(a["a"])("i",{className:"icon-calendar-month icon-line"})
var y=Object(a["a"])("i",{className:"icon-off icon-line"})
var x=Object(a["a"])("i",{className:"icon-publish icon-Solid"})
var N=Object(a["a"])("i",{className:"icon-unpublish"})
var w=Object(a["a"])("i",{className:"icon-calendar-day"})
g.render=function(){const e=this.props.model&&this.props.model.displayName()||m.t("This file")
return this.props.userCanManageFilesForContext?this.state.published&&this.state.restricted?n.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status restricted",title:this.getRestrictedText(),"aria-label":m.t("%{fileName} is %{restricted} - Click to modify",{fileName:e,restricted:this.getRestrictedText()})},v):this.state.published&&this.state.hidden?n.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status hiddenState",title:m.t("Not visible in student files"),"aria-label":m.t("%{fileName} is not visible in student files - Click to modify",{fileName:e})},y):this.state.published?n.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status published",title:m.t("Published"),"aria-label":m.t("%{fileName} is Published - Click to modify",{fileName:e})},x):n.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status unpublished",title:m.t("Unpublished"),"aria-label":m.t("%{fileName} is Unpublished - Click to modify",{fileName:e})},N):this.state.published&&this.state.restricted?n.a.createElement("div",{style:{marginRight:"12px"},"data-tooltip":"left",ref:"publishCloud",className:"published-status restricted",title:this.getRestrictedText(),"aria-label":m.t("%{fileName} is %{restricted}",{fileName:e,restricted:this.getRestrictedText()})},w):Object(a["a"])("div",{style:{width:28,height:36}})}
t["a"]=s()(g)},HaSH:function(e,t,i){"use strict"
i.d(t,"a",(function(){return l}))
var a=i("dfg0")
class l extends a["a"]{initialize(e,t){return super.initialize(...arguments)}}},Yi8D:function(e,t,i){"use strict"
i.d(t,"a",(function(){return s}))
var a=i("btHx")
var l=i("GLiE")
var n=i.n(l)
var _=i("jFQ7")
class s extends a["a"]{initialize(){this.on("change:sort change:order",this.setQueryStringParams)
return super.initialize(...arguments)}fetch(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{}
e.data=n.a.extend({content_types:null!=this.parentFolder?this.parentFolder.contentTypes:void 0},e.data||{});(null!=this.parentFolder?this.parentFolder.useVerifiers:void 0)&&(e.data.use_verifiers=1)
return super.fetch(e)}parse(e){if(e&&this.parentFolder){const t=this.parentFolder.previewUrl()
n.a.each(e,e=>e.rce_preview_url=t?t.replace("{{id}}",e.id.toString()):e.url)}return super.parse(...arguments)}setQueryStringParams(){const e={include:["user"],per_page:20,sort:this.get("sort"),order:this.get("order")}
if(this.loadedAll)return
const t=new URL(this.url)
const i=deparam(t.search)
t.search=$.param(n.a.extend(i,e))
this.url=t.toString()
return this.reset()}}s.optionProperty("parentFolder")
s.prototype.model=_["a"]},dfg0:function(e,t,i){"use strict"
var a=i("FIFq")
var l=i.n(a)
var n=i("GLiE")
var _=i.n(n)
var s=i("Cf7h")
var o=function(e,t){for(var i in t)r.call(t,i)&&(e[i]=t[i])
function a(){this.constructor=e}a.prototype=t.prototype
e.prototype=new a
e.__super__=t.prototype
return e},r={}.hasOwnProperty
t["a"]=function(e){o(t,e)
function t(){return t.__super__.constructor.apply(this,arguments)}t.prototype.displayName=function(){return this.get("display_name")||this.get("name")}
t.prototype.destinationIsSameContext=function(e){var t,i,a,l,n,_,o,r
o=(t=this.get("context_asset_string"))?Object(s["a"])(t,false):[null!=(l=this.collection.parentFolder)?l.get("context_type"):void 0,null!=(n=this.collection.parentFolder)&&null!=(_=n.get("context_id"))?_.toString():void 0],a=o[0],i=o[1]
return a&&i&&a.toLowerCase()===e.get("context_type").toLowerCase()&&i===(null!=(r=e.get("context_id"))?r.toString():void 0)}
t.prototype.moveTo=function(e,t){null==t&&(t={})
return this.destinationIsSameContext(e)?this.moveToFolder(e,t):this.copyToContext(e,t)}
t.prototype.moveToFolder=function(e,t){var i
null==t&&(t={})
i=this.setAttributes({parent_folder_id:e.id},t)
$.extend(i,{parent_folder_id:e.id})
return this.save({},{attrs:i}).then((a=this,function(){a.collection.remove(a)
return a.updateCollection(a,e,t)}))
var a}
t.prototype.copyToContext=function(e,t){var i,a,l,n,s,o
null==t&&(t={})
i=this.setAttributes($.extend({},this.attributes),t)
s=this.isFile?"file":"folder"
i["source_"+s+"_id"]=i.id
delete i.id
a=new this.constructor(_.a.omit(i,"id","parent_folder_id","parent_folder_path"))
l=this.updateCollection(a,e,t)
a.url=l.url
this.set("url",l.url)
n="copy_"+s
o="/api/v1/folders/"+e.attributes.id+"/"+n
return a.save(i,{url:o})}
t.prototype.setAttributes=function(e,t){null==e&&(e={})
null==t&&(t={})
"overwrite"===t.dup?$.extend(e,{on_duplicate:"overwrite"}):"rename"===t.dup&&(t.name?$.extend(e,{display_name:t.name,name:t.name,on_duplicate:"rename"}):$.extend(e,{on_duplicate:"rename"}))
return e}
t.prototype.updateCollection=function(e,t,i){var a,l
l=this.isFile?"files":"folders"
a=t[l]
"overwrite"===i.dup&&a.remove(a.where({display_name:e.get("display_name")}))
a.add(e,{merge:true})
return a}
return t}(l.a.Model)},jFQ7:function(e,t,i){"use strict"
var a=i("ouhR")
var l=i.n(a)
var n=i("GLiE")
var _=i.n(n)
var s=i("dfg0")
var o=i("60Hp")
i("jYyc")
var r=function(e,t){return function(){return e.apply(t,arguments)}},c=function(e,t){for(var i in t)u.call(t,i)&&(e[i]=t[i])
function a(){this.constructor=e}a.prototype=t.prototype
e.prototype=new a
e.__super__=t.prototype
return e},u={}.hasOwnProperty,d=[].slice
t["a"]=function(e){c(t,e)
function t(){this.externalToolEnabled=r(this.externalToolEnabled,this)
return t.__super__.constructor.apply(this,arguments)}t.prototype.url=function(){return this.isNew()?t.__super__.url.apply(this,arguments):"/api/v1/files/"+this.id}
t.prototype.initialize=function(e,i){null==i&&(i={})
this.preflightUrl=i.preflightUrl
return t.__super__.initialize.apply(this,arguments)}
t.prototype.save=function(e,i){var a,n,_,s,r,c
null==e&&(e={})
null==i&&(i={})
if(!this.get("file"))return t.__super__.save.apply(this,arguments)
this.set(e)
a=l.a.Deferred()
r=(u=this,function(e){u.set(e)
a.resolve(e)
return"function"===typeof i.success?i.success(e):void 0})
var u
s=function(e){a.reject(e)
return"function"===typeof i.error?i.error(e):void 0}
n=this.get("file")
_=(n.value||n.name).split(/[\/\\]/).pop()
n=n.files[0]
c={name:_,on_duplicate:"rename"}
Object(o["uploadFile"])(this.preflightUrl,c,n).then(r)["catch"](s)
return a}
t.prototype.isFile=true
t.prototype.toJSON=function(){var e
if(!this.get("file"))return t.__super__.toJSON.apply(this,arguments)
return _.a.pick.apply(_.a,[this.attributes,"file"].concat(d.call(_.a.keys(null!=(e=this.uploadParams)?e:{}))))}
t.prototype.present=function(){return _.a.clone(this.attributes)}
t.prototype.externalToolEnabled=function(e){var t
if(e.accept_media_types&&e.accept_media_types.length>0){t=this.get("content-type")
return _.a.find(e.accept_media_types.split(","),(function(e){var i
i=new RegExp("^"+e.replace("*",".*")+"$")
return t.match(i)}))}return true}
return t}(s["a"])},lUQV:function(e,t,i){"use strict"
var a=i("17x9")
var l=i.n(a)
var n=i("mNVu")
var _=i("dfg0")
t["a"]={contextType:l.a.oneOf(["users","groups","accounts","courses"]),contextId:l.a.oneOfType([l.a.string,l.a.number]),folder:l.a.instanceOf(n["a"]),filesystemObject:l.a.instanceOf(_["a"])}},mNVu:function(e,t,i){"use strict"
var a=i("dfg0")
i("FIFq")
var l=i("GLiE")
var n=i.n(l)
var _={}
var s=function(e){var t=n.a.uniqueId()
var i=n.a.extend((function(i,a){var l=function(){return new e(i,a)}
var n=i&&i[e.prototype.idAttribute]
if(n){var s=t+":"+n
if(_[s]){var o=_[s]
a&&a.parse&&(i=o.parse(i))
o.set(i)}else _[s]=l()
return _[s]}var r=l()
r.on("change:"+e.prototype.idAttribute,(function(e,i){_[t+":"+i]=r
r.off(null,null,this)}),this)
return r}),e)
i.prototype=e.prototype
return i}
s.resetCache=function(){_={}}
var o=s
var r=i("btHx")
var c=i("Yi8D")
var u=i("yE80")
var d={encodeSpecialChars:e=>e.replace(/%/g,"&#37;"),decodeSpecialChars:e=>e.split("/").map(e=>encodeURIComponent(decodeURIComponent(e).replace(/&#37;/,"%"))).join("/")}
const f=/^[^\/]+\/?/
let m=null
function b(e,t){return"name"!==t||e instanceof h?"user"===t?g(e.get("user"),e=>e.display_name)||"":"usage_rights"===t?g(e.get("usage_rights"),e=>e.license_name)||"":e.get(t):e.get("display_name")}class p extends a["a"]{initialize(e){this.contentTypes||(this.contentTypes=null!=e?e.contentTypes:void 0)
this.useVerifiers||(this.useVerifiers=null!=e?e.useVerifiers:void 0)
this.setUpFilesAndFoldersIfNeeded()
this.on("change:sort change:order",this.setQueryStringParams)
return super.initialize(...arguments)}url(){return this.isNew()?super.url(...arguments):"/api/v1/folders/".concat(this.id)}parse(e){const t=super.parse(...arguments)
this.contentTypes||(this.contentTypes=e.contentTypes)
this.useVerifiers||(this.useVerifiers=e.useVerifiers)
this.setUpFilesAndFoldersIfNeeded()
this.folders.url=e.folders_url
this.files.url=e.files_url
return t}setUpFilesAndFoldersIfNeeded(){this.folders||(this.folders=new k([],{parentFolder:this}))
if(!this.files)return this.files=new c["a"]([],{parentFolder:this})}getSubtrees(){return this.folders}getItems(){return this.files}expand(){let e=arguments.length>0&&void 0!==arguments[0]&&arguments[0]
let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}
let i
this.isExpanded=true
this.trigger("expanded")
if(this.expandDfd||e)return $.when()
this.isExpanding=true
this.trigger("beginexpanding")
this.expandDfd=$.Deferred().done(()=>{this.isExpanding=false
return this.trigger("endexpanding")})
const a=this.folders.url===this.folders.constructor.prototype.url||this.files.url===this.files.constructor.prototype.url;(a||e)&&(i=this.fetch())
return $.when(i).done(()=>{let e,i
0!==this.get("folders_count")&&(i=this.folders.fetch())
0===this.get("files_count")||t.onlyShowSubtrees||(e=this.files.fetch())
return $.when(i,e).done(this.expandDfd.resolve)})}collapse(){this.isExpanded=false
return this.trigger("collapsed")}toggle(e){return this.isExpanded?this.collapse():this.expand(false,e)}previewUrl(){let e
if(e=this.get("context_type"),["Course","Group"].includes(e))return"/".concat("".concat(this.get("context_type").toLowerCase(),"s"),"/",this.get("context_id"),"/files/{{id}}/preview")}isEmpty(){return!!(this.files.loadedAll&&0===this.files.length)&&this.folders.loadedAll&&0===this.folders.length}urlPath(){let e=(this.get("full_name")||"").replace(f,"")
e=d.encodeSpecialChars(e)
e=e.split("/").map(e=>encodeURIComponent(e)).join("/")
m||(m=i("BHWx").default)
if(m.showingAllContexts){const t="".concat(g(this.get("context_type"),e=>e.toLowerCase()),"s_").concat(this.get("context_id"))
e="".concat(t,"/").concat(e)}return e}childrenSorter(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"name"
let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"asc"
let i=arguments.length>2?arguments[2]:void 0
let a=arguments.length>3?arguments[3]:void 0
let l
const n=["name","user","usage_rights"].includes(e)
i=b(i,e)
a=b(a,e)
l=n?u["a"].strings(i,a):(()=>{if(i===a)return 0
if(i>a||void 0===i)return 1
if(i<a||void 0===a)return-1
throw new Error("wat? error sorting")})()
"desc"===t&&(l=0-l)
return l}children(e){let t=e.sort,i=e.order
return this.folders.toArray().concat(this.files.toArray()).sort(this.childrenSorter.bind(null,t,i))}}p.resolvePath=function(e,t,i){i=d.decodeSpecialChars(i)
const a="/api/v1/".concat(e,"/").concat(t,"/folders/by_path").concat(i)
return $.getJSON(a).pipe(e=>e.map(e=>new h(e,{parse:true})))}
p.prototype.defaults={name:""}
const h=o(p)
t["a"]=h
class k extends r["a"]{static initClass(){this.optionProperty("parentFolder")
this.prototype.model=h}parse(e){e&&e.forEach(e=>{e.contentTypes=this.parentFolder.contentTypes
return e.useVerifiers=this.parentFolder.useVerifiers})
return super.parse(...arguments)}}k.initClass()
h.FoldersCollection=k
function g(e,t){return"undefined"!==typeof e&&null!==e?t(e):void 0}},p6Wi:function(e,t,i){"use strict"
var a=i("pQTu")
var l=i("m0r6")
Object(l["a"])(JSON.parse('{"ar":{"buttons":{"cancel":"إلغاء","delete":"حذف"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"هل ترغب بالتأكيد في حذف هذا؟"}}},"cy":{"buttons":{"cancel":"Canslo","delete":"Dileu"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Ydych chi’n siŵr eich bod am ddileu hyn?"}}},"da":{"buttons":{"cancel":"Annuller","delete":"Slet"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Er du sikker på, at du vil slette dette?"}}},"da-x-k12":{"buttons":{"cancel":"Annuller","delete":"Slet"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Er du sikker på, at du vil slette dette?"}}},"de":{"buttons":{"cancel":"Abbrechen","delete":"Löschen"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Möchten Sie dies wirklich löschen?"}}},"el":{"buttons":{"cancel":"Ακύρωση","delete":"Διαγραφή"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Είστε σίγουρος/η ότι επιθυμείτε να το διαγράψετε;"}}},"en-AU":{"buttons":{"cancel":"Cancel","delete":"Delete"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Are you sure you want to delete this?"}}},"en-AU-x-unimelb":{"buttons":{"cancel":"Cancel","delete":"Delete"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Are you sure you want to delete this?"}}},"en-CA":{"buttons":{"cancel":"Cancel","delete":"Delete"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Are you sure you want to delete this?"}}},"en-GB":{"buttons":{"cancel":"Cancel","delete":"Delete"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Are you sure you want to delete this?"}}},"en-GB-x-lbs":{"buttons":{"cancel":"Cancel","delete":"Delete"}},"en-GB-x-ukhe":{"buttons":{"cancel":"Cancel","delete":"Delete"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Are you sure you want to delete this?"}}},"es":{"buttons":{"cancel":"Cancelar","delete":"Eliminar"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"¿Seguro que desea eliminarlo?"}}},"fa":{"buttons":{"cancel":"لغو","delete":"حذف"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"مطمئنید که می خواهید این مورد حذف شود؟"}}},"fi":{"buttons":{"cancel":"Peruuta","delete":"Poista"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Haluatko varmasti poistaa tämän?"}}},"fr":{"buttons":{"cancel":"Annuler","delete":"Supprimer"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Voulez-vous vraiment supprimer cet élément ?"}}},"fr-CA":{"buttons":{"cancel":"Annuler","delete":"Supprimer"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Voulez-vous vraiment supprimer cet élément?"}}},"he":{"buttons":{"cancel":"ביטול","delete":"ביטול"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"בטוח/ה שרוצה לבטל זאת?"}}},"ht":{"buttons":{"cancel":"Anile","delete":"Efase"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Ou kwè vrèman ou vle efase sa a?"}}},"hu":{"buttons":{"cancel":"Mégse","delete":"Törlés"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Biztos benne, hogy törli ezt?"}}},"hy":{"buttons":{"cancel":"Չեղյալ համարել","delete":"Ջնջել"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Դուք իսկապե՞ս ցանկանում եք ջնջել սա:"}}},"is":{"buttons":{"cancel":"Hætta við","delete":"Eyða"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Viltu örugglega eyða þessu?"}}},"it":{"buttons":{"cancel":"Annulla","delete":"Elimina"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Vuoi eliminare questo?"}}},"ja":{"buttons":{"cancel":"キャンセル","delete":"削除"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"これを削除してもよろしいですか?"}}},"ko":{"buttons":{"cancel":"취소","delete":"삭제"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"삭제하시겠습니까?"}}},"mi":{"buttons":{"cancel":"Whakakore","delete":"Muku"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"E tino hiahia ana koe ki te muku i tēnei?"}}},"nb":{"buttons":{"cancel":"Avbryt","delete":"Slett"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Er du sikker på at du ønsker å slette dette?"}}},"nb-x-k12":{"buttons":{"cancel":"Avbryt","delete":"Slett"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Er du sikker på at du ønsker å slette dette?"}}},"nl":{"buttons":{"cancel":"Annuleren","delete":"Verwijderen"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Weet je zeker dat je dit wilt verwijderen?"}}},"nn":{"buttons":{"cancel":"Avbryt","delete":"Slett"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Er du sikker på at du vil slette dette?"}}},"pl":{"buttons":{"cancel":"Anuluj","delete":"Usuń"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Czy na pewno chcesz usunąć ten element?"}}},"pt":{"buttons":{"cancel":"Cancelar","delete":"Excluir"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Tem certeza de que deseja excluir isto?"}}},"pt-BR":{"buttons":{"cancel":"Cancelar","delete":"Excluir"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Tem certeza que deseja excluir isto?"}}},"ru":{"buttons":{"cancel":"Отменить","delete":"Удалить"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Действительно хотите удалить?"}}},"sl":{"buttons":{"cancel":"Prekliči","delete":"Odstrani"}},"sv":{"buttons":{"cancel":"Avbryt","delete":"Radera"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Är du säker på att du vill radera det här?"}}},"sv-x-k12":{"buttons":{"cancel":"Avbryt","delete":"Radera"}},"tr":{"buttons":{"cancel":"İptal","delete":"Sil"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"Bunu silmek istediğinize emin misiniz?"}}},"uk":{"buttons":{"cancel":"Скасувати","delete":"Видалити"}},"zh-Hans":{"buttons":{"cancel":"取消","delete":"删除"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"是否确定要删除它?"}}},"zh-Hant":{"buttons":{"cancel":"取消","delete":"刪除"},"instructure_misc_plugins":{"confirms":{"default_delete_thing":"您是否確定要刪除？"}}}}'))
i("jQeR")
i("0sPK")
var n=a["default"].scoped("instructure_misc_plugins")
var _=i("ouhR")
var s=i.n(_)
var o=i("5Ky4")
var r=i("JD5e")
i("jYyc")
i("YGE8")
i("B1vq")
i("s/PJ")
s.a.fn.setOptions=function(e,t){let i=e?"<option value=''>"+Object(o["a"])(e)+"</option>":""
null==t&&(t=[])
t.forEach(e=>{const t=Object(o["a"])(e)
i+='<option value="'+t+'">'+t+"</option>"})
return this.html(s.a.raw(i))}
s.a.fn.ifExists=function(e){this.length&&e.call(this,this)
return this}
s.a.fn.scrollbarWidth=function(){const e=s()('<div style="width:50px;height:50px;overflow:hidden;position:absolute;top:-200px;left:-200px;"><div style="height:100px;"></div>').appendTo(this),t=e.find("div")
const i=t.innerWidth()
e.css("overflow-y","scroll")
const a=t.innerWidth()
e.remove()
return i-a}
s.a.fn.dim=function(e){return this.animate({opacity:.4},e)}
s.a.fn.undim=function(e){return this.animate({opacity:1},e)}
s.a.fn.confirmDelete=function(e){e=s.a.extend({},s.a.fn.confirmDelete.defaults,e)
const t=this
let i=null
let a=true
e.noMessage=e.noMessage||e.no_message
const l=function(){if(!a){e.cancelled&&s.a.isFunction(e.cancelled)&&e.cancelled.call(t)
return}e.confirmed||(e.confirmed=function(){t.dim()})
e.confirmed.call(t)
if(e.url){e.success||(e.success=function(e){t.fadeOut("slow",()=>{t.remove()})})
const a=e.prepareData?e.prepareData.call(t,i):{}
a.authenticity_token=Object(r["a"])()
s.a.ajaxJSON(e.url,"DELETE",a,i=>{e.success.call(t,i)},(i,a,l,n)=>{e.error&&s.a.isFunction(e.error)?e.error.call(t,i,a,l,n):s.a.ajaxJSON.unhandledXHRs.push(a)})}else{e.success||(e.success=function(){t.fadeOut("slow",()=>{t.remove()})})
e.success.call(t)}}
if(e.message&&!e.noMessage&&!s.a.skipConfirmations){if(e.dialog){a=false
const t="object"===typeof e.dialog?e.dialog:{}
i=s()(e.message).dialog(s.a.extend({},{modal:true,close:l,buttons:[{text:n.t("#buttons.cancel","Cancel"),click(){s()(this).dialog("close")}},{text:n.t("#buttons.delete","Delete"),class:"btn-primary",click(){a=true
s()(this).dialog("close")}}]},t))
return}a=confirm(e.message)}l()}
s.a.fn.confirmDelete.defaults={get message(){return n.t("confirms.default_delete_thing","Are you sure you want to delete this?")}}
s.a.fn.fragmentChange=function(e){if(e&&true!==e){const i=(window.location.search||"").replace(/^\?/,"").split("&")
let a=null
for(var t=0;t<i.length;t++){const e=i[t]
e&&0===e.indexOf("hash=")&&(a="#"+e.substring(5))}this.bind("document_fragment_change",e)
const l=this
let n=false
for(t=0;t<s.a._checkFragments.fragmentList.length;t++){const e=s.a._checkFragments.fragmentList[t]
e.doc[0]==l[0]&&(n=true)}n||s.a._checkFragments.fragmentList.push({doc:l,fragment:""})
s()(window).bind("hashchange",s.a._checkFragments)
setTimeout(()=>{a&&a.length>0?l.triggerHandler("document_fragment_change",a):l&&l[0]&&l[0].location&&l[0].location.hash.length>0&&l.triggerHandler("document_fragment_change",l[0].location.hash)},500)}else this.triggerHandler("document_fragment_change",this[0].location.hash)
return this}
s.a._checkFragments=function(){const e=s.a._checkFragments.fragmentList
for(let t=0;t<e.length;t++){const i=e[t]
const a=i.doc
if(a[0].location.hash!=i.fragment){a.triggerHandler("document_fragment_change",a[0].location.hash)
i.fragment=a[0].location.hash
s.a._checkFragments.fragmentList[t]=i}}}
s.a._checkFragments.fragmentList=[]
s.a.fn.clickLink=function(){const e=this.eq(0)
e.hasClass("disabled_link")||e.click()}
s.a.fn.showIf=function(e){if(s.a.isFunction(e))return this.each((function(t){s()(this).showIf(e.call(this))}))
e?this.show():this.hide()
return this}
s.a.fn.disableIf=function(e){s.a.isFunction(e)&&(e=e.call(this))
this.prop("disabled",!!e)
return this}
s.a.fn.indicate=function(e){e=e||{}
let t
if("remove"==e){t=this.data("indicator")
t&&t.remove()
return}s()(".indicator_box").remove()
let i=this.offset()
e&&e.offset&&(i=e.offset)
const a=this.width()
const l=this.height()
const n=(e.container||this).zIndex()
t=s()(document.createElement("div"))
t.css({width:a+6,height:l+6,top:i.top-3,left:i.left-3,zIndex:n+1,position:"absolute",display:"block","-moz-border-radius":5,opacity:.8,border:"2px solid #870",backgroundColor:"#fd0"})
t.addClass("indicator_box")
t.mouseover((function(){s()(this).stop().fadeOut("fast",(function(){s()(this).remove()}))}))
this.data("indicator")&&this.indicate("remove")
this.data("indicator",t)
s()("body").append(t)
e&&e.singleFlash?t.hide().fadeIn().animate({opacity:.8},500).fadeOut("slow",(function(){s()(this).remove()})):t.hide().fadeIn().animate({opacity:.8},500).fadeOut("slow").fadeIn("slow").animate({opacity:.8},2500).fadeOut("slow",(function(){s()(this).remove()}))
e&&e.scroll&&s()("html,body").scrollToVisible(t)}
s.a.fn.hasScrollbar=function(){return this.length&&this[0].clientHeight<this[0].scrollHeight}
s.a.fn.log=function(e){console.log("%s: %o",e,this)
return this}
s.a.fn.fillWindowWithMe=function(e){const t=s.a.extend({minHeight:400},e),i=s()(this),a=s()("#wrapper"),l=s()("#main"),n=s()("#not_right_side"),_=s()(window),o=s()(this).add(t.alsoResize)
function r(){o.height(0)
const e=_.height()-(a.offset().top+a.outerHeight())+(l.height()-n.height()),r=Math.max(400,e)
o.height(r)
s.a.isFunction(t.onResize)&&t.onResize.call(i,r)}r()
_.unbind("resize.fillWindowWithMe").bind("resize.fillWindowWithMe",r)
return this}
s.a.fn.autoGrowInput=function(e){e=s.a.extend({maxWidth:1e3,minWidth:0,comfortZone:70},e)
this.filter("input:text").each((function(){let t=e.minWidth||s()(this).width(),i="",a=s()(this),l=s()("<tester/>").css({position:"absolute",top:-9999,left:-9999,width:"auto",fontSize:a.css("fontSize"),fontFamily:a.css("fontFamily"),fontWeight:a.css("fontWeight"),letterSpacing:a.css("letterSpacing"),whiteSpace:"nowrap"}),n=function(){setTimeout(()=>{if(i===(i=a.val()))return
l.text(i)
const n=l.width(),_=n+e.comfortZone>=t?n+e.comfortZone:t,s=a.width(),o=_<s&&_>=t||_>t&&_<e.maxWidth
o&&a.width(_)})}
l.insertAfter(a)
s()(this).bind("keyup keydown blur update change",n)}))
return this}
s.a},ppAs:function(e,t,i){"use strict"
var a=i("ouhR")
var l=i.n(a)
var n=i("GLiE")
var _=i.n(n)
var s=i("5Ky4")
var o=i("pQTu")
var r=i("m0r6")
Object(r["a"])(JSON.parse('{"ar":{"user_content_aaf0fb5a":"محتوى المستخدم"},"cy":{"user_content_aaf0fb5a":"Cynnwys Defnyddiwr"},"da":{"user_content_aaf0fb5a":"Brugerindhold"},"da-x-k12":{"user_content_aaf0fb5a":"Brugerindhold"},"de":{"user_content_aaf0fb5a":"Benutzer-Content"},"el":{"user_content_aaf0fb5a":"Περιεχόμενο Χρήστη"},"en-AU":{"user_content_aaf0fb5a":"User Content"},"en-AU-x-unimelb":{"user_content_aaf0fb5a":"User Content"},"en-CA":{"user_content_aaf0fb5a":"User Content"},"en-GB":{"user_content_aaf0fb5a":"User content"},"en-GB-x-lbs":{"user_content_aaf0fb5a":"User content"},"en-GB-x-ukhe":{"user_content_aaf0fb5a":"User content"},"es":{"user_content_aaf0fb5a":"Contenido del usuario"},"fa":{"user_content_aaf0fb5a":"محتوای کاربر"},"fi":{"user_content_aaf0fb5a":"Käyttäjän sisältö"},"fr":{"user_content_aaf0fb5a":"Contenu de l\'utilisateur"},"fr-CA":{"user_content_aaf0fb5a":"Contenu de l\'utilisateur"},"he":{"user_content_aaf0fb5a":"תוכן משתמש"},"ht":{"user_content_aaf0fb5a":"Kontni Itilizatè"},"hu":{"user_content_aaf0fb5a":"Felhasználói tartalom"},"is":{"user_content_aaf0fb5a":"Notandaefni"},"it":{"user_content_aaf0fb5a":"Contenuto utente"},"ja":{"user_content_aaf0fb5a":"ユーザーコンテンツ"},"mi":{"user_content_aaf0fb5a":"Ihirangi kaiwhakamahi"},"nb":{"user_content_aaf0fb5a":"Brukerinnhold"},"nb-x-k12":{"user_content_aaf0fb5a":"Brukerinnhold"},"nl":{"user_content_aaf0fb5a":"Gebruikersinhoud"},"nn":{"user_content_aaf0fb5a":"Brukarinnhald"},"pl":{"user_content_aaf0fb5a":"Zawartość użytkownika"},"pt":{"user_content_aaf0fb5a":"Conteúdo do Utilizador"},"pt-BR":{"user_content_aaf0fb5a":"Conteúdo do Usuário"},"ru":{"user_content_aaf0fb5a":"Контент пользователя"},"sl":{"user_content_aaf0fb5a":"Vsebina uporabnika"},"sv":{"user_content_aaf0fb5a":"Användarinnehåll"},"sv-x-k12":{"user_content_aaf0fb5a":"Användarinnehåll"},"tr":{"user_content_aaf0fb5a":"Kullanıcı İçeriği"},"uk":{"user_content_aaf0fb5a":"Контент користувача"},"zh-Hans":{"user_content_aaf0fb5a":"用户内容"},"zh-Hant":{"user_content_aaf0fb5a":"使用者內容"}}'))
i("jQeR")
i("0sPK")
var c=o["default"].scoped("user_content")
const u={translateMathmlForScreenreaders(e){const t=l()("<div/>").html(e.attr("x-canvaslms-safe-mathml")).html()
const i=l()('<span class="hidden-readable"></span>')
i.html(t)
return i},toMediaCommentLink(e){const t=l()("<a\n        id='media_comment_".concat(Object(s["a"])(l()(e).data("media_comment_id")),"'\n        data-media_comment_type='").concat(Object(s["a"])(l()(e).data("media_comment_type")),"'\n        class='instructure_inline_media_comment ").concat(Object(s["a"])(e.nodeName.toLowerCase()),"_comment'\n        data-alt='").concat(Object(s["a"])(l()(e).attr("data-alt")),"'\n      />"))
t.html(l()(e).html())
return t},convert(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}
const i=l()("<div />").html(e)
i.find("video.instructure_inline_media_comment,audio.instructure_inline_media_comment").replaceWith((function(){return u.toMediaCommentLink(this)}))
i.find("object.instructure_user_content:not(#kaltura_player) embed").remove()
if(!t.forEditing){i.find("object.instructure_user_content,embed.instructure_user_content").replaceWith((function(){const e=l()(this)
if(!e.data("uc_snippet")||!e.data("uc_sig"))return this
const t=_.a.uniqueId("uc_")
let i="/object_snippet"
ENV.files_domain&&(i="//".concat(ENV.files_domain).concat(i))
const a=l()("<form\n            action='".concat(Object(s["a"])(i),"'\n            method='post'\n            class='user_content_post_form'\n            target='").concat(Object(s["a"])(t),"'\n            id='form-").concat(Object(s["a"])(t),"'\n          />"))
a.append(l()("<input type='hidden'/>").attr({name:"object_data",value:e.data("uc_snippet")}))
a.append(l()("<input type='hidden'/>").attr({name:"s",value:e.data("uc_sig")}))
l()("body").append(a)
setTimeout(()=>a.submit(),0)
return l()("<iframe\n            class='user_content_iframe'\n            name='".concat(Object(s["a"])(t),"'\n            style='width: ").concat(Object(s["a"])(e.data("uc_width")),"; height: ").concat(Object(s["a"])(e.data("uc_height")),";'\n            frameborder='0'\n            title='").concat(Object(s["a"])(c.t("User Content")),"'\n          />"))}))
i.find("img.equation_image").each((e,t)=>{const i=l()(t)
const a=u.translateMathmlForScreenreaders(i)
i.removeAttr("x-canvaslms-safe-mathml")
i.after(a)})}return i.html()}}
t["a"]=u},yE80:function(e,t,i){"use strict"
var a=i("pQTu")
t["a"]={strings(e,t){let i=a["default"].locale||"en-US"
const l={zh_Hant:"zh-Hant"}
i=l[i]||i
return e.localeCompare(t,i,{sensitivity:"variant",ignorePunctuation:false,numeric:true})},by(e){return(t,i)=>this.strings(e(t),e(i))},byKey(e){return this.by(t=>t[e])},byGet(e){return this.by(t=>t.get(e))}}}}])

//# sourceMappingURL=67-c-9710e32b3b.js.map
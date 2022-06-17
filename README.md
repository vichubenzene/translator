# Translator
Translates any language to any language 

<h3>Pypi version of this will be released soon</h3> 

```py
from translator.benzene_translator import google_translator

detector = google_translator()
detect_result = detector.detect("hello")
translator = google_translator()

print(detect_result)


pronounce = translator.translate("hello",
                                         lang_src=detect_result,
                                         lang_tgt="ta",
                                         pronounce=True)
print(pronounce)
```

Result:
```
['en', 'english']
['வணக்கம் ', 'həˈlō', 'Vaṇakkam']
```

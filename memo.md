# get start
pip install fastapi  
pip install uvicorn サーバー  

ucicorn main:app --reload  
※ main.pyのappインスタンスを起動 --realodでホットリロード有効化  

~/docsでアクセスすることで自動的にswaggerのドキュメントを見れる
→ このドキュメントはmain.pyによって生成される
→postメソッドに対しては、dataに値入れてswagger上でテストできる

apiのは上から順に実行されるのでパスがかぶると上の方が優先的に動く
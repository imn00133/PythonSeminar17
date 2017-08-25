Python3의 파일 입출력 관련 인코딩 문제
====================================

## introduction
파일 입출력을 할 때, windows(7, 10)에서는 cp494로 저장되는 것을 확인할 수 있었다. 이것은 파이썬3에서 작동하는 것과는 완전히 다른데, 이 인코딩에 대한 문제를 해결하기 위해서 한참을 뒤적거렸다. 점프 투 파이썬에서는 딱히 이야기가 없다.  
사실 인코딩 문제가 많이 복잡하지...

## 블로그에서 제시해준 해결책
python txt 파일 읽기 애러: <http://newpower.tistory.com/123>  
위 문서에서는 utf-8을 붙여주거나, 파일 인코딩을 ansi로 바꿔주면 된다고 한다. 하지만 왜 그런지 원인이 없어서 이 문서는 원하는 답이 없다.

python3.x버전에서 utf-8 파일 읽기 <http://pracon.tistory.com/153>  
ansi만 읽을 수 있으나, codecs 라이브러리를 통해서 읽을 수 있다고 한다.

파이썬에서 한글을 처리하실 때, 필히 유니코드를 쓰세요. <https://allieus.wordpress.com/2015/03/23/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%ED%95%9C%EA%B8%80%EC%9D%84-%EC%B2%98%EB%A6%AC%ED%95%98%EC%8B%A4-%EB%95%8C-%ED%95%84%ED%9E%88-%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C%EB%A5%BC-%EC%93%B0/>  
파이썬에서 한글이 깨진다고요? - 파이썬의 한글 입출력과 인코딩에 대해 <https://soooprmx.com/archives/4912>  
python2와 python3의 차이점을 보여주면서 python2에서 utf-8을 사용하는 법에 대해서 이야기 해주고 있다. 보고 있으면 python2에서 한글인코딩이 답이 없어요! 라는 걸 볼 수 있다.  
이 문서들에서는 python3에서는 인코딩을 명시하지 않으면 utf-8이라고 말하고 있지만 cp494로 출력이 되고 있다.  
또한 표준출력시에 sys.stdout.encodng, sys.stdin.encoding (파이썬에서 한글이 깨진다고요? 에서는 shell의 인코딩 환경이라고 한다.) sys.stderr.encoding의 값에 따라서 표준출력이 된다고 한다. 파일 입출력 이야기는 없다.

예제로 배우는 Python 프로그래밍 <http://pythonstudy.xyz/python/article/206-%ED%8C%8C%EC%9D%BC-%EB%8D%B0%EC%9D%B4%ED%83%80-%EC%B2%98%EB%A6%AC>  
시스템 디폴트 인코딩 방식을 따라서 파일 인코딩이 된다고 한다. sys.getdefaultencoding()을 확인한 결과 utf-8로 잡혀있다.  

python3에 뛰어들기(dive to python3) <https://codeonweb.com/entry/db0582a9-6ad1-46da-9481-3419a4eb9c14>  
이곳에 답이 있었지만, 밤에 대충 읽어서 답을 읽지 못했다. 그 후에 python3 레퍼런스 보면서 뒤적였는데, 좀 더 자세히, 일찍 봤었으면 덜 뒤적였을 것 같다.  
locale.getpreferredencoding()에 따라서 초기 encoding이 잡힌다고 한다.

## python3 레퍼런스 문서
python 3.6.2의 documentation중 Built-in Functions를 확인하였다.
<https://docs.python.org/3/library/functions.html#open>  
이 중 open함수를 보았는데, encoding부분에서 locale.getpreferredencoding()을 디폴트값을 가지고 있다고 한다.
그 함수를 확인하니 cp494를 반환하고 있는 것을 볼 수 있었다. 여기서 문제가 발생했다. 
locale.getpreferredencoding 함수: <https://docs.python.org/3/library/locale.html#locale.getpreferredencoding>  

## cp494로 되어있는 파일내 문자열을 읽었을 때 문제점이 있는지 확인
python3에서 cp494로 되어있는 문자열을 읽고, 그 읽은 문자열을 비교하거나 검색하였을 때, 문제가 있는지 확인하였다. 문자를 찾거나 문자열을 비교하였을 때, 문제는 없다.

## 결론
파일 입출력을 할 때는 open("file_name", "방식", encoding="")을 사용하는게 좋고, 어떤 파일이 들어올지 모른다면, locale을 통해 기본 값을 받은 후에 utf-8을 확인하는 방식등을 사용해야 될 것으로 보인다.

## Unicode에 대한 좀 더 자세한 사항을 보려면
파이썬에서 unicode에 대한 글을 적어두었다.
<https://docs.python.org/3/howto/unicode.html>
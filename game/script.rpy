# 이 파일에 게임 스크립트를 입력합니다.

# master: 기본 레이어 (배경 이미지나 메인 캐릭터 이미지 등)
# transient: 일시적인 이미지들이 표시되는 레이어 (예: 팝업, 대사)
# overlay: UI 요소들이 표시되는 레이어 (예: 대화창, 메뉴)
# layer1, layer2: 사용자가 추가한 새로운 레이어들

# init python:
#     # 새로운 레이어 정의
#     config.layers = ['master', 'transient', 'overlay', 'layer1', 'layer2']

# 외부 모듈 불러오기
# --> 파일을 읽어오지 못했다.
# init python:
#     import file_reader  
init python:
    import gen_imagefileName as genImageFile
    import textwrap
    import random
    import webbrowser 

    def open_link(url):
        webbrowser.open(url)  # 기본 브라우저에서 링크 열기     

    def wrap_text(text, width=40):
        # textwrap을 사용하여 문자열을 지정된 너비로 나눔
        wrapped_text = textwrap.fill(text, width=width)
        return wrapped_text

    def show_banner_ad():
        if renpy.android:
            renpy.run("""from android import AndroidService
service = AndroidService("show_banner_ad")
service.start()""")

    def hide_banner_ad():
        if renpy.android:
            renpy.run("""from android import AndroidService
service = AndroidService("hide_banner_ad")
service.start()""")

# 게임에서 사용할 캐릭터를 정의합니다.

# ctc option은 fixed, nestled-close, nestled 가 있다.

define act_PreNarator = Character(None, kind = nvl, retain=False, color = "#f18f0e", what_color="#0918e9", ctc="ctc_click_img", ctc_pause="ctc_click_img", ctc_position="nestled-close")

define act_Narator = Character(None, kind = nvl, retain=False, color = "#e47113",what_color="#0918e9", ctc="ctc_click_img", ctc_position="nestled-close") 

# 6개의 괘를 표시할 이미지 12개를 정의한다.
image imageGau1_1 = "images/1.png"
image imageGau1_2 = "images/2.png"
image imageGau2_1 = "images/1.png"
image imageGau2_2 = "images/2.png"
image imageGau3_1 = "images/1.png"
image imageGau3_2 = "images/2.png"
image imageGau4_1 = "images/1.png"
image imageGau4_2 = "images/2.png"
image imageGau5_1 = "images/1.png"
image imageGau5_2 = "images/2.png"
image imageGau6_1 = "images/1.png"
image imageGau6_2 = "images/2.png"

# 캐릭터가 대사를 마치고, 클릭 이미지를 표시합니다.
image ctc_click_img:
    "images/hand-click.png"
    zoom 0.2
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat 

image bgDualCircle:
    "images/EmptyBg.jpg"

image bgBegin:
    "images/EmptyBg.jpg"    

image bgMain:
    "images/EmptyBg.jpg"

image coin0:
    "images/COIN0.png"    

image coin1:
    "images/COIN1.png"

image coin2:
    "images/COIN2.png"

image coin3:
    "images/COIN3.png"

image coin5:
    "images/COIN5.png"

image coin4:
    "images/COIN4.png"

image coin_gif_animation:
    "images/COIN1.png"
    0.25 # 0.2초 대기
    "images/COIN2.png"
    0.15
    "images/COIN3.png"
    0.25
    "images/COIN4.png"
    0.15
    repeat

# 텍스트 효과
transform blink_0_1:
    alpha 1.0 # 완전히 보임
    linear 1.0 alpha 0.0 # 서서히 사라짐
    linear 0.0 alpha 1.0 # 서서히 나타남
    repeat # 반복

transform slow_fade_in:
    alpha 0.0 # 초기 투명도
    linear 5.0 alpha 1.0

transform shake_fade_out:
    # linear 0.1 xoffset 10  # 오른쪽으로 이동
    # linear 0.1 xoffset -10  # 왼쪽으로 이동
    # repeat 3  # 5번 반복
    alpha 1.0  # 초기 투명도
    linear 5.0 alpha 0.0  # 3초 동안 투명도를 0으로 변경    

transform slow_fade_out:
    alpha 1.0  # 초기 투명도
    linear 10.0 alpha 0.0  # 10초 동안 투명도를 0으로 변경

transform shake_effect:
    linear 0.1 xoffset 10  # 오른쪽으로 이동
    linear 0.1 xoffset -10  # 왼쪽으로 이동
    repeat 5  # 5번 반복

transform rotate_effect_360:
    rotate 0  # 초기 각도
    zoom 1.0
    linear 1.0 zoom 1.5
    linear 10.0 rotate 360  # 360도 회전
    repeat

transform rotate_effect:
    alpha 1.0  # 초기 투명도 (완전 투명)
    rotate 0  # 초기 각도
    zoom 1.0
    linear 1.0 zoom 2.0
    linear 10.0 rotate 720  # 360도 회전
    linear 1.0 alpha 0.0
    repeat

transform move_center_effect:
    xalign 0.5 yalign 0.5  # 화면 중앙
    linear 1.0 xalign 0.8 yalign 0.2  # 오른쪽 상단으로 이동
    linear 1.0 xalign 0.2 yalign 0.8  # 왼쪽 하단으로 이동
    linear 1.0 xalign 0.5 yalign 0.5  # 중앙으로 복귀

image imgClickIt:
    "images/hand-click.png"
    zoom 3.0

image splash:
    "images/FirstBg.jpg"
    # zoom 0.5

label splashscreen:
    # 동영상으로 loading 하려면
    # $ renpy.movie_cutscene('splash.webm')
    # scene bgDualCircle
    # play music "audio/whip-afro-dancehall-music-110235.mp3" fadein 1.0
    with Pause(1)
    show splash with dissolve
    with Pause(1)
    show text "{size=75}{b}더{color=#000000}運勢{/color}(운세){/b}{/size}\n\n{size=60}{color=#000000}옛 사람들의 지혜를 나누는\n\n{b}운세(運勢)풀이{/b}.{/color}{/size}" at blink_0_1
    with Pause(3)
    hide text with dissolve
    # scene bgDualCircle with dissolve
    # stop music fadeout 1.0
    with Pause(1)
    return



################################################################################
## 시작 버튼은 script.rpy에서 구현.
################################################################################
screen my_start_button():
    # 배경 이미지 추가
    # image "images/EmptyBg.jpg"  # 배경 이미지 파일
    # add bgBegin

    # 화면에 버튼 추가
    vbox:
        align (0.5, 0.7)  # 화면 중앙에 배치
        spacing 100  # 버튼 사이 간격

        # "게임 시작" 이미지 버튼
        imagebutton:
            idle "images/start_btn.png"  # 기본 상태 이미지
            hover "images/start_btn.png"  # 호버 상태 이미지
            action Start()  # 게임 시작

        # "게임 종료" 이미지 버튼
        imagebutton:
            idle "images/quit_btn.png"  # 기본 상태 이미지
            hover "images/quit_btn.png"  # 호버 상태 이미지
            action Quit(confirm=False)  # 게임 종료 

screen imagemap_main():
    imagemap:
        ground "images/MainMenu.jpg"
        hover "images/MainMenu.jpg"

        #image map의 영역 정의
        hotspot(200,1300, 550,1450) action Call('juyuk_origin') 
        hotspot(800,1300, 1200,1450) action Call('juyuk_love') 

        hotspot(200,1700, 550,1850) action Call('juyuk_business') 
        hotspot(800,1700, 1200,1850) action Call('juyuk_stock') 

        hotspot(200,1950, 550,2100) action Call('juyuk_today') 
        hotspot(800,1950, 1200,2100) action Call('app_ending') 


init python:
    def btn_clicked_function():
        renpy.notify("Button clicked!")

screen ending_button():
    vbox:
        align (0.5, 0.5) # 화면 중앙에 위치
        spacing 100 # 버튼 사이 간격

        # "다시보기" 이미지 버튼
        imagebutton:
            idle "images/again_btn.png"  # 기본 상태 이미지
            hover "images/again_btn.png"  # 호버 상태 이미지
            action Call("juyuk_jump_bricks")
            # action [Jump("juyuk_jump_bricks"), Function(btn_clicked_function)]

        # "About" 이미지 버튼
        imagebutton:
            idle "images/about_btn.png"  # 기본 상태 이미지
            hover "images/about_btn.png"  # 호버 상태 이미지
            action Call("about_app")
            # action [Jump("about_app"), Function(btn_clicked_function)]

        # "후원하기" 이미지 버튼
        imagebutton:
            idle "images/share_btn.png"  # 기본 상태 이미지
            hover "images/share_btn.png"  # 호버 상태 이미지
            action Call("share_app")
            # action [Jump("share_app"), Function(btn_clicked_function)]

        # "다시하기" 이미지 버튼
        imagebutton:
            idle "images/start_btn.png"  # 기본 상태 이미지
            hover "images/start_btn.png"  # 호버 상태 이미지
            # $ renpy.full_restart()
            action [Jump("start"), Function(btn_clicked_function)]

        # "게임 종료" 이미지 버튼
        imagebutton:
            idle "images/quit_btn.png"  # 기본 상태 이미지
            hover "images/quit_btn.png"  # 호버 상태 이미지
            # $ game_quit = True
            action Quit(confirm=False)  # 게임 종료


# 여기에서부터 게임이 시작합니다.
label start:

    $ itemString = ""
    $ game_quit = False

    #주역점을 한번만 보도록 한다. 두번째는 메시지를 출력한다.
    $ game_1 = 0
    $ game_2 = 0
    $ game_3 = 0
    $ game_4 = 0
    $ game_5 = 0

    while game_quit == False:
        call screen imagemap_main
 
    return

label juyuk_love:
    call generater_juyuk_gae(0.2)
    $ itemString = "111111"
    scene bgMain with fade
    call juyuk_jump_bricks(2)

    # call juyuk_origin
    return

label juyuk_business:
    call generater_juyuk_gae(0.3)
    $ itemString = "111111"
    scene bgMain with fade
    call juyuk_jump_bricks(3)
    return

label juyuk_stock:
    call generater_juyuk_gae(0.4)
    $ itemString = "111111"
    scene bgMain with fade
    call juyuk_jump_bricks(4)
    return

label juyuk_today:
    call generater_juyuk_gae(0.1)
    $ itemString = "111111"
    scene bgMain with fade
    call juyuk_jump_bricks(5)
    return

label app_ending:
    $ game_quit = True
    $ renpy.quit()
    return

label juyuk_origin:
    scene bgBegin 

    # play music "audio/relaxing-piano-music-275681.mp3" fadein 1.5 loop

    show coin1:
        alpha 0.0  # 초기 투명도 (완전 투명)
        xpos 0.20
        ypos 0.1
        zoom 2.0
        linear 3.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)    

    call juyuk_description 

    hide coin1

    call assemble_ramdom_bricks

    show coin0:
        alpha 0.0  # 초기 투명도 (완전 투명)
        xpos 0.20
        ypos 0.1
        zoom 2.0
        linear 3.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명) 
    
    show text "{size=70}{color=#000000}{b}풀이를 볼께요~{/b}{/color}{/size}" with irisout

    show ctc_click_img:
        alpha 0.0
        xpos 0.8
        ypos 0.8
        linear 3.0 alpha 1.0

    $ renpy.pause(2.0)
    hide ctc_click_img
    hide text with dissolve

    hide coin0

    with Pause(1)

    scene bgMain with fade

    call juyuk_jump_bricks(1) from _call_juyuk_jump_bricks

    call juyuk_ending from _call_juyuk_ending

    with Pause(1)    
    return

label juyuk_jump_bricks(g_option=1):

    if itemString == "1111110": #테스트용 샘플
        call g_1111110(g_option) from _call_g_1111110
    elif itemString == "111111": #중천건
        call g_111111(g_option) from _call_g_111111
    elif itemString == "222222": #중지곤
        call g_222222(g_option) from _call_g_222222
    elif itemString == "212221": #수뢰둔
        call g_212221(g_option) from _call_g_212221
    elif itemString == "122212": #산수목
        call g_122212(g_option) from _call_g_122212
    elif itemString == "212111": #수천수
        call g_212111(g_option) from _call_g_212111
    elif itemString == "111212": #천수송
        call g_111212(g_option) from _call_g_111212
    elif itemString == "222212": #지수사
        call g_222212(g_option) from _call_g_222212
    elif itemString == "212222": #수지비
        call g_212222(g_option) from _call_g_212222
    elif itemString == "112111": #풍천소축
        call g_112111(g_option) from _call_g_112111
    elif itemString == "111211": #천택리
        call g_111211(g_option) from _call_g_111211
    elif itemString == "222111": #지천태
        call g_222111(g_option) from _call_g_222111
    elif itemString == "111222": #천지비
        call g_111222(g_option) from _call_g_111222
    elif itemString == "111121": #천화동인 
        call g_111121(g_option) from _call_g_111121
    elif itemString == "121111": #화천대유
        call g_121111(g_option) from _call_g_121111
    elif itemString == "222122": #지산겸
        call g_222122(g_option) from _call_g_222122
    elif itemString == "221222": #뇌지예
        call g_221222(g_option) from _call_g_221222
    elif itemString == "211221": #택뢰수
        call g_211221(g_option) from _call_g_211221
    elif itemString == "122112": #산풍고
        call g_122112(g_option) from _call_g_122112
    elif itemString == "222211": #지택림
        call g_222211(g_option) from _call_g_222211
    elif itemString == "112222": #풍지관
        call g_112222(g_option) from _call_g_112222
    elif itemString == "121221": #화뢰서합
        call g_121221(g_option) from _call_g_121221
    elif itemString == "122121": #산화비
        call g_122121(g_option) from _call_g_122121
    elif itemString == "122222": #산지박
        call g_122222(g_option) from _call_g_122222
    elif itemString == "222221": #지뢰복
        call g_222221(g_option) from _call_g_222221
    elif itemString == "111221": #천뢰무망
        call g_111221(g_option) from _call_g_111221
    elif itemString == "122111": #산천대축
        call g_122111(g_option) from _call_g_122111
    elif itemString == "122221": #산뢰이
        call g_122221(g_option) from _call_g_122221
    elif itemString == "211112": #택풍대과
        call g_211112(g_option) from _call_g_211112
    elif itemString == "212212": #중수감
        call g_212212(g_option) from _call_g_212212
    elif itemString == "121121": #중화리
        call g_121121(g_option) from _call_g_121121
    elif itemString == "211122": #택산함
        call g_211122(g_option) from _call_g_211122
    elif itemString == "221112": #뇌풍항
        call g_221112(g_option) from _call_g_221112
    elif itemString == "111122": #천산돈
        call g_111122(g_option) from _call_g_111122
    elif itemString == "221111": #뇌천대장
        call g_221111(g_option) from _call_g_221111
    elif itemString == "121222": #화지진
        call g_121222(g_option) from _call_g_121222
    elif itemString == "222121": #지화명이
        call g_222121(g_option) from _call_g_222121
    elif itemString == "112121": #풍화가인
        call g_112121(g_option) from _call_g_112121
    elif itemString == "121211": #화택규
        call g_121211(g_option) from _call_g_121211
    elif itemString == "212122": #수산건
        call g_212122(g_option) from _call_g_212122
    elif itemString == "221212": #뇌수해
        call g_212212(g_option) from _call_g_212212_1
    elif itemString == "122211": #산택손
        call g_122211(g_option) from _call_g_122211
    elif itemString == "112221": #풍뢰익
        call g_112221(g_option) from _call_g_112221
    elif itemString == "211111": #택천쾌
        call g_211111(g_option) from _call_g_211111
    elif itemString == "111112": #천풍구
        call g_111112(g_option) from _call_g_111112
    elif itemString == "211222": #택지취
        call g_211222(g_option) from _call_g_211222
    elif itemString == "222112": #지풍승
        call g_222112(g_option) from _call_g_222112
    elif itemString == "211212": #택수곤
        call g_211212(g_option) from _call_g_211212
    elif itemString == "212112": #수풍정
        call g_212112(g_option) from _call_g_212112
    elif itemString == "211121": #택화혁
        call g_211121(g_option) from _call_g_211121
    elif itemString == "121112": #화풍정
        call g_121112(g_option) from _call_g_121112
    elif itemString == "221221": #중뢰진
        call g_221221(g_option) from _call_g_221221
    elif itemString == "122122": #중산간
        call g_122122(g_option) from _call_g_122122
    elif itemString == "112122": #풍산점
        call g_112122(g_option) from _call_g_112122
    elif itemString == "221211": #뇌택귀매
        call g_221211(g_option) from _call_g_221211
    elif itemString == "221121": #뇌화풍
        call g_221121(g_option) from _call_g_221121
    elif itemString == "121122": #화산려
        call g_121122(g_option) from _call_g_121122
    elif itemString == "112112": #중풍손
        call g_112112(g_option) from _call_g_112112
    elif itemString == "211211": #중택태
        call g_211211(g_option) from _call_g_211211
    elif itemString == "112212": #풍수환
        call g_112212(g_option) from _call_g_112212
    elif itemString == "212211": #수택절
        call g_212211(g_option) from _call_g_212211
    elif itemString == "112211": #풍택중부
        call g_112211(g_option) from _call_g_112211
    elif itemString == "221122": #뇌산소과
        call g_221122(g_option) from _call_g_221122
    elif itemString == "212121": #수화기제
        call g_212121(g_option) from _call_g_212121
    elif itemString == "121212": #화수미제
        call g_121212(g_option) from _call_g_121212               
    else:
        call juyuk_ending from _call_juyuk_ending_1

    return    

label juyuk_description:
    with Pause(1)
    show text "{size=75}음과 양의 섭리를 설명하는 주역 64괘로{/size}" with irisout
    with Pause(2)
    hide text with dissolve
    show text "{size=75}상황이 어떻게 나아갈지 살펴 볼까요?{/size}" with irisout
    with Pause(2)
    hide text with dissolve    
    show text "{size=75}{b}바른 운세(運勢)를 구하려면{/b}, 호흡과 주변을 정리하고,{/size}" with irisout
    with Pause(2)
    hide text with dissolve
    show text "{size=75}{b}마음을 차분히 하고{/b} 진행해 주세요!{/size}" with irisout
    with Pause(2)
    hide text with dissolve
    return

label juyuk_ending:
    
    while game_quit == False:

        scene bgBegin
        call screen ending_button

    scene bgBegin with dissolve

    return

label share_app:

    menu:
        "광고보기":
            # $ admob_html_file = "admob_ad_sample.html"
            # $ webbrowser.open("file://" + renpy.loader.transfn(admob_html_file))
            $ show_banner_ad()
        "광고숨기기":
            $ hide_banner_ad()           
        "취소":
            pass
    return

label about_app:

    default gMessageAbout = """

    {size=85}{b}더운세(運勢)는{/b}{/size}

    {size=60}옛 선인들의 지혜에서 상황을 비추어봅니다.
    
    옛 선인들의 기록이 알려주는 조화로운 
    
    음양의 통찰을 경험하시길 바랍니다.

    한꺼번에 여러 질문을 하기 보다는,

    알고자 하는 질문을 정하고,

    마음을 편안히 한 후 구하기 바랍니다.{/size}
    """
    show text "[gMessageAbout]" at move_center_effect
    $ renpy.pause()
    hide text dissolve
    
    return

label generater_juyuk_gae(pause_value=0.5):
    $ itemCount = 0
    $ itemString = ""
    # 괘는 한번에 조합한다.
    while itemCount < 6:
        # if itemCount % 3 == 0:
        #     nvl clear
        $ randomValue = renpy.random.randint(0,999)%2+1
        $ itemString += str(randomValue)
        $ itemCount += 1
        with Pause(pause_value)

    return

label show_juyuk_gae(xvalue=0.4, yvalue=0.6, zoomvalue=1.5, gapvalue=0.025):

    $ g1_xpos = xvalue
    $ g1_ypos = yvalue
    $ g1_zoom = zoomvalue
    $ g1_gueGap = gapvalue
        
    $ itemCount = 0
    while itemCount < 6:
    # $ for char in itemString:
        $ g1_ypos = g1_ypos + g1_gueGap
        $ char = itemString[itemCount]
        $ itemCount += 1
        if itemCount == 1:
            if char == "1":
                show imageGau1_1:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
            else:
                show imageGau1_2:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
        elif itemCount == 2:
            if char == "1":
                show imageGau2_1:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
            else:
                show imageGau2_2:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
        elif itemCount == 3:
            if char == "1":
                show imageGau3_1:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
            else:
                show imageGau3_2:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
        elif itemCount == 4:
            if char == "1":
                show imageGau4_1:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
            else:
                show imageGau4_2:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
        elif itemCount == 5:
            if char == "1":
                show imageGau5_1:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
            else:
                show imageGau5_2:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
        elif itemCount == 6:
            if char == "1":
                show imageGau6_1:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
            else:
                show imageGau6_2:
                    alpha 0.0  # 초기 투명도 (완전 투명)
                    xpos g1_xpos
                    ypos g1_ypos
                    zoom g1_zoom
                    linear 2.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)
        else:
            show text "어 이럴리가 없어요"

    $ renpy.pause(0.5)
    return    

label assemble_ramdom_bricks:
    $ explainMessage = [
        '상황을 차분히 바라보는 시선이 필요 할수도 있습니다.',
        '주위 시선을 의식해서 불편을 감수하지 마세요',
        '상황에 당당히 맞서려는 굳건함도 가끔 필요해요.',
        '한쪽으로 치우치지 않는 균형감각은 꼭 필요해요.',
        '현실과 상상을 분별하는 관점이 중요해요.',
        '지혜는 꼭 오래 살아서 알게 되는 것은 아니예요',
        '삶이 평탄하다고 정말 잘 살고 있는것일까요',
        '앞으로 나아가는것은 마음먹기 부터 시작하는게 분명해요.',
        '하늘을 올려다 보세요. 끝간데 없이 위에 있어요',
        '아래를 내려다 보세요. 굳건한 땅의 지지가 있어요',
        '너무 심각하지 않게, 자세는 편안하게, 천천히 호흡에 집중해 보세요',
        '지금이 적당한 때가 아닐 수 있고, 그렇다면 지나쳐 가는것도 괜찮아요.',
        '길이 막혀있다면, 다른 길로 돌아 가야 할 수도 있어요.',
        '시선은 허공 멀리에 두고 귀는 내 심장 박동에 기울여 보세요.',
        '분위기에 휘둘리지 말고, 지혜를 구하는 마음으로 보시기 바랍니다.'
    ]

    show text "{size=70}{color=#330994}그럼 괘를 구해봅시다!{/color}{/size}" with irisout
    with Pause(0.8)
    hide text

    # 괘를 조합하기 전에 소개 문장
    $ randomChoice = renpy.random.choice(explainMessage)
    show text "{cps=10}{size=70}[randomChoice]{/size}{/cps}" with  irisout
    # $ renpy.pause()
    with Pause(1.5)
    hide text

    # 돌아가는 이미지를 표시합니다.
    show coin_gif_animation:
        alpha 0.2  # 초기 투명도 (완전 투명)
        xpos 0.20
        ypos 0.1
        zoom 2.2
        linear 1.5 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)

    # 괘는 한번에 조합한다.
    call generater_juyuk_gae

    call show_juyuk_gae

    hide coin_gif_animation 

    show coin5:
        # alpha 0.0  # 초기 투명도 (완전 투명)
        xpos 0.20
        ypos 0.1
        zoom 2.2
        linear 5.0 alpha 1.0  # 2초 동안 투명도를 1.0으로 변경 (완전 불투명)

    show text "{size=70}{color=#330994}괘를 찾았어요.{/color}{/size}" with irisout
    # $ renpy.pause()     
    with Pause(1.0)
    hide text with dissolve

    hide coin5

    return

label display_bricks_message(actor, messages=[], speed=10):
    $ lineCount = len(messages)
    $ idxLoop = 0
    $ speed = 20

    while idxLoop < lineCount:

        if idxLoop % 8 == 0:
            nvl clear        

        if idxLoop == 0:
            actor "{cps=[speed]}{b}{size=+25}[messages[idxLoop]]{/size}{/b}{/cps}{nw}" with wiperight
        else:
            actor "{cps=[speed]}{size=+15}[messages[idxLoop]]{/size}{/cps}{nw}" with irisout

        with Pause(0.6)
        $ idxLoop = idxLoop + 1

    # actor "" with irisout

    return


label display_bricks_message_v3(messages):
    show text "[messages]" at slow_fade_in

    show ctc_click_img:
        alpha 0.0
        xpos 0.8
        ypos 0.8
        linear 3.0 alpha 1.0

    $ renpy.pause()
    hide text fade
    show text "[messages]" at shake_fade_out
    with Pause(5.0)
    hide text dissolve
    hide ctc_click_img

    return

label g_1111110(g__option=1):

    $ gMessage = """
    {size=75}{b}중천건(重天乾){/b}{/size}                      

    {size=60}중천건(重天乾)은 하늘을 상징하며,
    순수한 양(陽)의 에너지를 나타냅니다.
    이 괘는 강합, 창조성,활력,리더십
    그리고 끊임없는 발전을 의미합니다.
    하늘을 뜻하는 천(天)과 건(乾)이 겹쳐진 형상으로,
    두배로 강화된 것을 상징합니다.
    하늘처럼 높은 이상을 추구하며,
    끊임없이 나아가라는 메시지입니다.

    순수한 양의 에너지로 가득 차 있습니다.
    이는 강인한 의지 활력 그리고 끊임없는 발전을 의미합니다.
    하늘은 만물을 창조하는 근원입니다.
    새로운 시작, 창조, 그리고 무한한 가능성을 상징합니다.
    이 괘는 강한 리더십과 결단력을 나타냅니다.
    하늘 처럼 높은 이상을 추가하며, 사람들을 이끄는 힘을 상징합니다.
    하늘은 또한 끊임없이 움직이고 변화합니다.
    변화를 받아들이고 적용하는 능력을 강조합니다.
    
    아직 힘을 발휘할 때가 아닙니다.
    잠재된 상태에서 준비하고 기다리는 것이 중요합니다.
    서두르지 말고 때를 기다리세요.
    잠재된 능력이 조금씩 나타나기 시작합니다.
    큰 도약을 준비하는 시기입니다.
    신중하게 행동하고 기회를 놓치지 마세요.
    자신의 능력을 믿고 최선을 다하세요.
    균형을 유지하도록 주의하고, 겸손을 잃지 마세요.{/size}"""

    call display_bricks_message_v3(gMessage) from _call_display_bricks_message_v3
    
    return


label g_111111(g__option=1):
    $ g_exp_messages = """
    {size=75}{b}중천건(重天乾){/b}{/size}                      

    {size=60}중천건(重天乾)은 하늘을 상징하며,
    순수한 양(陽)의 에너지를 나타냅니다.
    이 괘는 강합, 창조성,활력,리더십
    그리고 끊임없는 발전을 의미합니다.
    하늘을 뜻하는 천(天)과 건(乾)이 겹쳐진 형상으로,
    두배로 강화된 것을 상징합니다.
    하늘처럼 높은 이상을 추구하며,
    끊임없이 나아가라는 메시지입니다.

    순수한 양의 에너지로 가득 차 있습니다.
    이는 강인한 의지 활력 그리고 끊임없는 발전을 의미합니다.
    하늘은 만물을 창조하는 근원입니다.
    새로운 시작, 창조, 그리고 무한한 가능성을 상징합니다.
    이 괘는 강한 리더십과 결단력을 나타냅니다.
    하늘 처럼 높은 이상을 추가하며, 사람들을 이끄는 힘을 상징합니다.
    하늘은 또한 끊임없이 움직이고 변화합니다.
    변화를 받아들이고 적용하는 능력을 강조합니다.

    아직 힘을 발휘할 때가 아닙니다.
    잠재된 상태에서 준비하고 기다리는 것이 중요합니다.
    서두르지 말고 때를 기다리세요.
    잠재된 능력이 조금씩 나타나기 시작합니다.
    큰 도약을 준비하는 시기입니다.
    신중하게 행동하고 기회를 놓치지 마세요.
    자신의 능력을 믿고 최선을 다하세요.
    균형을 유지하도록 주의하고, 겸손을 잃지 마세요.{/size}"""

    $ g2_exp_messages = """
    {size=75}{b}중천건(重天乾){/b}{/size}                      

    {size=60}순수한 양(陽)의 에너지를 나타냅니다.
    끊임없이 나아가라는 메시지입니다.
    새로운 시작, 창조, 그리고 무한한 가능성을 상징합니다.
    변화를 받아들이고 적용하는 능력을 강조합니다.
    잠재된 능력이 조금씩 나타나기 시작합니다.
    큰 도약을 준비하는 시기입니다.
    신중하게 행동하고 기회를 놓치지 마세요.
    자신의 능력을 믿고 최선을 다하세요.
    균형을 유지하도록 주의하고, 겸손을 잃지 마세요.{/size}"""    

    $ g3_exp_messages = """
    {size=75}{b}중천건(重天乾){/b}{/size}                      

    {size=60}끊임없이 나아가라는 메시지입니다.
    새로운 시작, 창조, 그리고 무한한 가능성을 상징합니다.
    변화를 받아들이고 적용하는 능력을 강조합니다.
    잠재된 능력이 조금씩 나타나기 시작합니다.
    큰 도약을 준비하는 시기입니다.
    신중하게 행동하고 기회를 놓치지 마세요.
    자신의 능력을 믿고 최선을 다하세요.
    균형을 유지하도록 주의하고, 겸손을 잃지 마세요.{/size}"""

    $ g4_exp_messages = """
    {size=75}{b}중천건(重天乾){/b}{/size}                      

    {size=60}큰 도약을 준비하는 시기입니다.
    신중하게 행동하고 기회를 놓치지 마세요.
    자신의 능력을 믿고 최선을 다하세요.
    균형을 유지하도록 주의하고, 겸손을 잃지 마세요.{/size}"""

    $ g5_exp_messages = """
    {size=75}{b}중천건(重天乾){/b}{/size}                      

    {size=60}큰 도약을 준비하는 시기입니다.
    신중하게 행동하고 기회를 놓치지 마세요.{/size}"""     

    if g__option == 1: 
        call display_bricks_message_v3(g_exp_messages) 
    elif g__option == 2: 
        call display_bricks_message_v3(g2_exp_messages) 
    elif g__option == 3: 
        call display_bricks_message_v3(g3_exp_messages) 
    elif g__option == 4: 
        call display_bricks_message_v3(g4_exp_messages) 
    else:
        call display_bricks_message_v3(g5_exp_messages)
    
    return

label g_222222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}곤위지(坤爲地){/b}{/size}

        {size=60}위의 괘는 땅(地)이고 아래 괘도 땅(地)이다.
        모두 땅을 상징하는 곤괘(坤卦)로 구성되어 있어 지(地)라고 하였다.
        여섯 개의 효(爻)가 모두 음(陰)으로,
        하늘의 기를 받아들여 만물을 포용하고 양육시키는 어머니와 같다.
        곤(坤)이 없으면 건(乾)의 위대한 힘이 발휘되지 못한다. 
        곤(坤)의 속성은 순응하다. 지극하다라는 뜻이다. 
        이 괘를 얻은 사람은 포용력과 인내를 가지고,
        유순한 마음으로 맡은 일에 충실해야 한다.
        또 봉사하는 자세로 사람들을 포용하고 사랑을 베풀어야 한다.
        자신의 능력을 과시하여 명성을 얻으려 하면 불상사가 생긴다.
        남을 돕더라도 남의 모르게 돕고,
        영광이 돌아오더라도 남에게 돌려야 한다.
        말과 행동을 조심해야 한다.
        현재의 운세는 비교적 침체된 상태지만 머지않아 성운(成運)을 맞을 수 있다.
        윗사람이나 선배의 뜻에 잘 따라라.
        자신의 공적을 과시하려는 생각을 가지지 말고 남을 도와 그늘에서 묵묵히 일하라.
        부하가 상사를 앞지르려고 한다거나,
        아내가 남편을 앞서려고 하면 반드시 불상사가 일어난다.
        사업 확장이나 신규 사업에 착수하는 것은 좋지 않으므로,
        당분간 내실을 꾀하면서 관망하는 것이 좋다.{/size}
        """

    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_2
    return

label g_212221(g__option=1):

    $ g_exp_messages = """
        {size=75}{b}수뇌둔(水雷屯){/b}{/size}

        {size=60}위는 물(水)이고 아래는 우레(雷)다. 
        둔(屯)은 ‘진치다’ ‘막히다’ ‘고민하다’라는 뜻이다.
        비가 내리고 천둥이 진동하는 상이니 새싹이 눈 속에서 봄을 기다리는 것과 같다.
        하늘과 땅이 자리를 정한 뒤에 천둥과 번개,
        그리고 폭우가 쏟아져 내리는 모습이라 할 수 있으니,
        지금은 모든 일에 어려움이 많다.
        마치 출산의 고통과도 같다. 
        그러나 출산의 고통 끝에 자식을 얻는 기쁨이 있는 것처럼 곧 좋은 때가 온다.
        날이 갈수록 운이 호전되기 때문에 초조하지 말고,
        인내력을 가지고 고통을 이겨내야 한다.
        지금은 매우 어려운 상황에 처해있기 때문에,
        큰 목적이나 희망을 가지고 있더라도 주위의 상황이 불리하여 뜻을 이룰 수 없는 때다.
        무리하게 앞으로 나아가려는 것은 오히려 화를 초래한다.
        고진감래(苦盡甘來)의 진리를 명심하고,
        당분간 은인자중하며 때가 오기를 기다리는 것이 좋다.
        사업도 매사에 막히는 일이 많고 다사다난(多事多難)하므로,
        매우 좋은 계획을 가지고 있더라도 당분간 관망하는 것이 좋다.
        비가 온 뒤에 땅이 굳어진다는 속담처럼 불행 뒤에,
        항상 행복이 따라온다는 자연의 진리를 명심해야 한다.
        시간이 지나면 자신의 포부를 펼 수 있는 기회가 온다.{/size}
        """
    
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_3
    return

label g_122212(g__option=1):

    $ g_exp_messages = """
        {size=75}{b}산수몽(山水蒙){/b}{/size}

        {size=60}위의 괘는 산(山)이고 아래 괘는 물(水)이다.
        몽(蒙)을 ‘어리다’ ‘어리석다’라는 뜻이다.
        시작의 상이며 교육과 밀접한 관계가 있다.

        마치 어린아이가 걸음마를 배우는 것처럼 매사에 서툴고 몽매하다.
        그래서 교육을 뜻하는 몽(蒙)자를 괘의 이름으로 하였고,
        계몽(啓蒙)이라는 말이 여기서 나왔다.
        이 괘를 얻은 사람은 지금은 새로운 출발점에 있으므로,
        모르는 것이 많을 것이나 하나하나 성실히 배워나간다면,
        머지않아 광명의 때를 맞아 크게 발전할 수 있다.
        지금 운세는 앞이 캄캄하고 뻗어나가지 못하는 상태다.
        서둘지 말고 윗사람이나 선배의 의견에 따르는 것이 좋다.
        항상 배운다는 자세로 임하면 장래가 크게 기대된다.{/size}
        """

    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_4
    return

label g_212111(g__option=1):

    $ g_exp_messages = """
        {size=75}{b}수천수(水天需)

        {size=60}위는 물(水)이고 아래는 하늘(天)이다. 
        수(需)는 ‘기다리다’ ‘기대하다’라는 뜻이다.
        운무가 자욱한 상이다.
        세상사에는 시운(時運)이 있는 법으로 힘차게 나아가야 할 때가 있는가 하면,
        물러서서 기다려야 할 때도 있다.
        이 괘를 얻은 사람은 매사에 막힘이 많고 되는 일이 없기 때문에 조급하기 쉬운데,
        이런 때일수록 침착하게 몸과 마음을 가다듬으며,
        충분한 휴식을 취하는 것이 좋다.
        축적된 힘이 크면 클수록 나중에 얻을 수 있는 성공 또한 크다.
        지금의 운세는 구름이 하늘을 덮고 있는 상이어서 매우 침체된 상태다.
        지금 서둘러 일을 도모하면 건강을 해치고 불리해진다.
        기다리면 반드시 운이 트인다.{/size}
        """
    
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_5
    return

label g_111212(g__option=1):

    $ g_exp_messages = """
        {size=75}{b}천수송(天水訟){/b}{/size}

        {size=60}위는 하늘(天)이고 아래는 물(水)다.
        송(訟)은 ‘다툼’ ‘소송’ ‘재판’ 등을 뜻한다.
        하늘 아래 물이 넘치는 상이니 욕심이 지나쳐 마찰과 갈등이 생기고,
        대립 항쟁하는 것으로 괘 이름을 송(訟,으로 하였다.
        시비의 근원에는 반드시 나만을 먼저 생각하는 이기심이 있으므로,
        항상 남을 생각하는 미덕을 가져야 한다.
        이 괘를 얻은 사람은 아무리 자신에게 타당한 이유가 있다하더라도,
        끝까지 자기의 뜻을 관철하려하지 말고,
        남의 의사를 존중하고 따르는 것이 좋다.
        싸워서 이겨도 득이 되지 않는다. 운세는 전반적으로 쇠운(衰運)이다.
        시비, 소송 등이 생기기 쉬우니 타인과 의견 충돌을 피해야 한다.
        자신을 억제하고 시간이 지나기를 기다리는 것이 최선이다.
        사업은 실력에 맞는 일이라면 아무 탈이 없겠지만,
        자기 분수에 맞지 않는 일에 착수하면 실패하기 쉽다.
        문서상의 일로 곤경에 빠질 우려가 있으니 조심해야 한다.{/size}
        """

    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_6
    return

label g_222212(g__option=1):

    $ g_exp_messages = """
        {size=75}{b}지수사(地水師){/b}{/size}

        {size=60}위는 땅(地)이고 아래는 물(水)이다. 
        사(師)는 ‘선생’ ‘군대’라는 뜻이다.
        땅 밑으로 물이 모이는 상이니 여러 사람이 모인 집단을 상징하므로,
        통솔한다는 의미에서 사(師)를 괘 이름으로 하였다.
        영웅이 전투에서 여러 사람을 지휘하는 상으로 싸우면 반드시 이겨야 한다.
        이 괘를 얻은 사람은 지도자의 위치에 있으므로,
        정확한 판단력과 과감한 실천력이 필요하며,
        매사에 있어서 주도면밀한 계획과 준비가 필요하다.
        또 일단 일을 시작하면 끝까지 밀고 나가야 한다.
        장수는 남보다 어려움이 많으므로,
        개인적인 감정이나 고집을 버리고 만사에 공명정대해야 한다.
        또 유능한 참모를 발탁하는 지혜를 길러야 한다.
        운세는 무척 강하기 때문에 어떤 일에도우두머리가 되어 일하게 된다.
        잠시도 쉴 틈이 없고 한가지 일이 끝나면 다음 일이 기다리며,
        어지간히 노력하지 않으면 실패, 좌절 등을 맛보게 된다.
        개인의 역량보다는 여러 사람의 일치된 힘에 의해 일의 성패가 좌우되기 때문에,
        뚜렷한 소신과 넓은 포용력으로 대인 관계를 폭넓게 쌓아간다면,
        어떠한 난관도 극복하고 성공할 수 있다.{/size}
        """

    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_7
    return

label g_212222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}수지비(水地比){/b}{/size}

        {size=60}위는 물(水)이고 아래는 땅(地)이다.
        비(比)는 ‘견주다’ ‘비교하다’ ‘인화(人和)’를 상징한다.
        물이 땅을 고루 적시고 논에 물이 가득 찬 것 같아 안정과 풍요로움을 나타낸다.
        땅위의 물은 낮은 곳으로 모여 내를 이루고 힘을 합치는 상이므로,
        뜻을 같이하는 사람이 집단을 이루어 서로 돕고 협력하므로 비(比)는 친화를 도모한다.
        이 괘를 얻은 사람은 여러 사람들로부터 신망을 얻고 있어,
        집단의 우두머리로 손색이 없으나 경쟁이 치열하다.
        운세는 점진적으로 발전한다.
        대인 관계를 중시하고 인화단결이 잘되면 어떤 사업이든 과감하게 추진해도 성공할 수 있다.
        그러나 혼자 힘으로는 안 된다.{/size}
    """

    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_8
    return

label g_112111(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}풍천소축(風天小畜){/b}{/size}

        {size=60}위는 바람(風)이고 아래는 하늘(天)이다.
        축(畜)은 ‘기르다’ ‘저축하다’라는 뜻이다.
        하늘에서 바람이 부는 모습이니 비가 내리기 전의 상황을 상징하고,
        비가 오면 만유의 생명체는 그 비를 저장하는 까닭에,
        저축한다는 의미로 축(畜)을 괘의 이름으로 하였다.
        이 괘를 얻은 사람은 하늘에서 바람이 불어 구름을 쫓는 상이어서,
        비는 안 오고 구름만 이리저리 몰려다니는 것처럼,
        일이 될 듯 하면서도 안 되는 일이 많고,
        대인 관계에서도 불화가 많다. 
        그렇기 때문에 안정된 생활을 영위하기 위해서는 미래를 준비하는 저축을 하여야 한다.
        운세는 경제적으로 안정된 시점에 와 있기는 하나,
        비가 오기전의 음울한 하늘과 같이 잡다한 어려움이 많다.
        운이 막혀있기 때문에 내실(저축)을 기하고 현상 유지에 힘써야 한다.
        새로운 사업에 손을 대면 고전하게 된다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_9
    return

label g_111211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}천택이(天澤履){/b}{/size}

        {size=60}위는 하늘(天)이고 아래는 못(澤)이다.
        이(履)는 ‘밟는다’ ‘따른다’ ‘예절’이라는 뜻이다.
        하늘 아래 저수지가 있는 상이니 지나침과 부족함이 없이 풍요로워 예절을 나타낸다.
        의식(衣食)이 족해야 예절을 안다는 말에서 유래된 것이다.
        이 괘를 얻는 사람은 타인들보다 앞서지 말고,
        남의 뒤를 따르며 평소보다 겸손하고 정성스럽게 예의에 어긋남이 없이 대해야 한다.
        앞장서 일을 하면 반드시 실패한다.
        운세는 현재 의식이 풍족하여 자만심에 빠져 있을 때이므로,
        자신도 모르게 위험한 일에 말려드는 경우가 있다.
        애매한 태도와 불손한 언사 그리고 분수에 맞지 않는 생활은 화를 자초할 수 있다.
        사업도 상당히 위험한 상태에 놓여있기 때문에 남의 의견을 존중하고,
        윗사람의 뒤를 따르면 처음에는 어렵더라도 나중에 좋은 결과를 얻을 수 있다.
        남과 시비를 다투어도 이길 수 없다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_10
    return

label g_222111(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}지천태(地天泰){/b}{/size}

        {size=60}위는 땅(地)이고 아래는 하늘(天)이다.
        태(泰)는 ‘크다’ ‘크게 통한다’ ‘태평하다’라는 뜻이다.
        땅의 기운은 하늘로 올라가고 하늘의 기운은 땅으로 내려와 서로 조화를 이루니,
        만물이 생성되는 화창한 봄날이다.
        그러므로  태평하다는 태(泰)를 괘의 이름으로 하였다.
        이 괘를 얻는 사람은 만사가 형통하는 시점에 놓여있기 때문에,
        지금의 현실에 만족하는 것이 최선이다.
        정상에 오르면 그 다음은 내리막길이므로 지금의 호운을 유지할 수 있도록 노력해야 한다.
        운세는 매우 순조롭고 이익도 크다.
        방심하지만 않으면 크게 성공한다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_11
    return

label g_111222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}천지비(天地否){/b}{/size}

        {size=60}위는 하늘(天)이고 아래는 땅(地)이다.
        비(否)는 ‘막히다’ ‘답답하다’라는 뜻이다.
        하늘은 하늘대로 위에 있고 땅은 땅대로 아래에 있으니,
        천지 화합이 일어나지 않아 막혀 있는 상태이므로,
        답답하다는 뜻으로 비(否)를 괘의 이름으로 하였다.
        이 괘를 얻은 사람은 모든 일이 침체되어 난처한 지경에 처해있다.
        하늘은 하늘 땅은 땅이라는 식으로,
        화합의 기미가 전혀 보이지 않고 반목의 상태가 지속된다.
        답답하고 안타깝겠지만 적당한 시기가 올 때까지 은인자중 하는 것이 상책이다.
        믿었던 사람들로부터 배반을 당하고,
        의사 소통이 되지 않아 마치 달이 먹구름 속에 숨은 상태다.
        사업 확장을 꾀하거나 신규 사업에 손을 댈 수 있는 상황이 아니므로,
        상황이 혼전될 때를 기다려야 한다.
        겨울이 오면 또 봄이 가까워진다는 사실을 명심할 일이다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_12
    return

label g_111121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}천화동인(天火同人){/b}{/size}

        {size=60}위는 하늘(天)이고 아래는 불(火)이다.
        동인(同人)은 ‘뜻을 같이 한다.’ ‘협력’이라는 뜻이다.
        어두운 하늘 아래 불이 타오르며 세상을 밝히는 상이다.
        즉 어두운 밤길에 등불을 얻은 상으로 세상을 밝히는 일은,
        여러 사람이 힘을 합쳐야 하므로 동인(同人)을 괘의 이름으로 하였다.
        이 괘를 얻은 사람은 여러 사람과 협력하여 일을 도모하면,
        주변의 도움을 받으며 큰 일을 성취할 수 있다.
        그러나 동인(同人)이라는 뜻에는 같은 목적을 가진 사람이기 때문에,
        경쟁자라는 의미도 포함되어 있다.
        자신의 실속보다는 의리를 중요시하고 사적인 이익보다는,
        공적인 이익을 중요시하는 마음 자세가 필요하다.
        사업은 내부의 분쟁만 없다면 얼마든지 발전할 수 있으며,
        운이 좋기 때문에 불의(不義)한 일만 아니라면,
        중도에 포기하지 말고 꾸준히 노력해야 한다.
        다만 경쟁자가 많기 때문에 약간의 고생은 예상해야 한다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_13
    return

label g_121111(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}화천대유(火天大有){/b}{/size}

        {size=60}위는 불(火)이고 아래는 하늘(天)이다.
        대유(大有)는 크게 만족하여 즐거워하는 상태를 말한다.
        하늘 위에 불(태양)이 온 천하를 밝게 비추는 상이다.
        즉 해가 중천에 떠 밝게 빛나는 상이니,
        천하를 소유한다는 의미의 대유(大有)를 괘의 이름으로 하였다.
        이 괘를 얻은 사람은 공명정대한 처신과,
        넓은 아량으로 천하를 포용하는 군자의 덕을 잃지 않아야,
        어떠한 일을 해도 크게 성공할 수 있다.
        시기하고 질투하는 소인배들이 주변에 많을 수 있다.
        그들까지 포용하여 배려해야 한다.
        대단한 성운(盛運)으로 특히 명예나 학문에 관계된 일에 좋다.
        옛사람들은 금(金)과 옥(玉)이 집안 가득한 것을,
        여기서 인용하여 대유(大有)라고 표현하였다.
        그러나 차면 이지러지는 것이 또한 역(易)의 원리다.
        언제 닥칠지 모르는 쇠운(衰運)에 대비해야 하며,
        특히 남으로부터 시기와 원망을 사지 않도록 주의해야 한다.
        사업은 무리한 일만 아니라면 추진해도 별 어려움 없이 성취할 수 있다.
        그러나 한 낮이 가면 어둠이 점점 다가온다는 사실을 명심해야 한다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_14
    return

label g_222122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}지산겸(地山謙){/b}{/size}

        {size=60}위는 땅(地)이고 아래는 산(山)이다.
        겸(謙)을 ‘겸손’ ‘겸양’으로 자기보다 부족한 사람을 이끌어주고 도와준다는 뜻이다.
        높은 산이 땅 밑에 파묻힌 모습이니 벼가 익어 고개를 숙이는 상이므로,
        겸손하다는 의미에서 겸(謙)을 괘의 이름으로 하였다.
        이 괘를 얻은 사람은 명예와 신용을 지키며 정도에 맞게 행동한다면 대체로 길하다.
        현재 어려운 상황에 있더라도 바른 마음을 가지고 있으면 곧 호운(好運)을 맞을 수 있다.
        지금까지 성공을 했다면 이제 후진을 양성하고 공익을 생각해야 한다.
        모든 일에 길한 괘이기는 하지만 한 개의 양(陽)이 다섯 개의 음(陰)에 둘러싸여 있으니,
        선천적으로 바람기가 많아 여난(女難)을 조심해야 한다.
        사업은 서둘지 말고 성실하게 일하고 전진보다는 내실을 꾀하는 것이 좋다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_15
    return

label g_221222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}뇌지예(雷地豫){/b}{/size}

        {size=60}위는 우뢰 천둥(雷)이고 아래는 땅(地)이다.
        예(豫)는 ‘예측한다’라는 뜻이다.
        땅 위 에서 천둥 번개가치면 비가 내리는 것을 예측할 수 있으므로,
        예(豫)를 괘의 이름으로 하였다.
        비가 내리면 대지를 골구려 적셔주어 땅속에 있던,
        씨앗이 싹을 터 이제 땅위로 올라올 수 있다.
        이 괘를 얻은 사람은 선견지명(先見之明)이 있는 해박한 사람으로,
        지금까지 노고가 인정되어 서서히 그 대가를 받을 수 있다.
        전부터 계획하고 있던 사업이나 자신의 포부를 펼 때다.
        예(豫)란 좋은 일에 대한 예측을 뜻하기도 하지만,
        나쁜 일을 미연에 방지하라는 뜻도 되기 때문에,
        유비무환(有備無患,의 준비를 철저히 해야한다.
        하나의 양에 다섯의 음에 둘러싸여 있기 때문에,
        여난(女難)을 당할 수 있으므로 이성관계에 특별히 조심해야 한다.
        사업은 치밀한 계획과 철저한 준비로 일을 추진하면 틀림없이 성공한다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_16
    return

label g_211221(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}택뇌수(澤雷隨){/b}{/size}

        {size=60}위눈 연못(澤)이고 아래는 우레 천둥(雷)이다.
        수(隨)는 ‘따르다’ ‘순종한다’라는 뜻으로 수동적이며 종속적인 의미를 가지고 있다.
        하늘에서 진동해야 할 우레가 연못 아래 있으니,
        꼼짝 못하고 연못의 뜻에 따를 수밖에 없어 수(隨)를 괘의 이름으로 하였다.
        그러나 천둥은 언젠가는 다시 진동할 수 있다.
        이 괘를 얻은 사람은 실력은 충분히 갖추고 있지만,
        약간 어려운 상황에 처해 있어 잠시 타의에 의해 움직이는 운세다.
        자신의 일보다는 남의 일로 바쁘고 남의 감언이설(甘言利說)에 속기 쉬운 때다.
        무슨 일이나 세심한 주의를 기울이고 좋은 협력자를 얻어 근면 성실하게 노력하면 나중에 성공할 수 있다.
        사업은 남들이 이미 착수한 일이나 시류(時流)에 맞는 일을 벌이면 성공할 수 있다.
        남이 자기를 따르게 하려면 자신이 먼저 남을 위해 솔선수범 해야 한다는 교훈을 명심해야 한다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_17
    return

label g_122112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}산풍고(山風蠱){/b}{/size}

        {size=60}위는 산(山)이고 아래는 바람(風)이다.
        고(蠱)는 ‘벌레’ ‘벌레가 나뭇잎을 갉아먹는다’는 뜻으로 어려운 일을 뜻한다.
        산밑에 바람이 머물고 있으니 공기가 혼탁한 것이,
        마치 벌레가 생긴 상한 음식과 같다하여 고(蠱)를 괘 이름으로 하였다.
        그릇(皿 : 그릇 명) 위에서 벌레(蟲 :벌레 충)가 굼틀거리고 있으니,
        좋은 일이 없고 건강, 재산, 의욕 등 모든 사라져 가는 상이다.
        이 괘를 얻은 사람은 뽕잎이 누에에 야금야금 먹혀 들어가듯,
        심각한 상황에 놓여 심각한 고통을 당하고 있다.
        이것들은 모두 자업자득(自業自得)으로 문제의 원인이 자신에게 있다.
        즉 지금 겪는 고난은 과거에 저지른 자신의 그릇된 일에서 비롯된 것이므로,
        환골탈퇴(換骨脫退)하려는 굳은 의지가 필요하다.
        지금의 고난을 전화위복(轉禍爲福)의 기회로 삼아,
        평소 잘 아는 사람을 조심하고 자신의 좋지 못한 생활 태도를 청산해야 한다.
        사업은 부정부패와 무능이 만연된 상태이므로,
        구태의연한 모든 것을 혁신해야하며 세대교체를 해야 만이 살아남는다.{/size}
        """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_18
    return

label g_222211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}지택임(地澤臨){/b}{/size}

        {size=60}위는 땅(地)이고 아래는 목(澤)이다.
        임(臨)은 ‘순서를 밟다’ ‘군림하다’라는 뜻이다.
        땅속에 있는 물이 지상으로 뚫고 올라오는 형상이므로,
        새로운 시작에 임한다는 뜻에서 임(臨)을 괘의 이름으로 하였다.
        그런데 임(臨)은 군림(君臨)한다는 의미가 있으므로 여러 사람 위에 있는 지도자의 상이다.
        이 괘를 얻은 사람은 정당한 방법으로 자신의 능력을 발휘하여,
        새로운 계획이나 포부를 실천에 옮기면 반드시 성공하여 우두머리가 된다.
        정치인이나 대표에게는 가장 좋은 괘다.
        여성이 이 괘를 얻으면 땅 밑에서 솟아오르려는 물처럼,
        앞 뒤 가리지 않고 유혹과 색정에 빠져들 수 있으니 조심해야 한다.
        사업은 왕성한 운세이므로 주저하지 말고 추진하는 것이 좋다.
        그러나 뜻하지 않은 변화가 속출하기 때문에,
        철저한 준비와 주변 사람들과 긴밀한 유대관계가 중요하다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_19
    return

label g_112222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}풍지관(風地觀){/b}{/size}

        {size=60}위는 바람(風)이고 아래는 땅(地)이다.
        관(觀)은 ‘살핀다’라는 뜻이다.
        땅위에 바람이 불어 새로운 변화가 일어나니,
        이러한 변화를 잘 관찰하여야 한다는 뜻에서 관(觀)을 괘의 이름으로 하였다.
        이 괘를 얻은 사람은 땅위에 바람이 불어 지금까지 잠잠했던 일에 큰 변화가 생기는 것을 암시한다.
        물질적인 것보다는 정신적인 면에서 더 큰 발전이 있으므로
        학문, 연구, 종교와 관련되는 일에는 매우 좋다.
        변화라는 것은 좋은 방향으로 발전하기도 하지만 나쁘게도 변할 수 있으므로,
        마음을 한 곳에 집중하고 태산 같은 자기 중심을 잡고 사태를 세밀하게 살펴야 한다.
        사업은 새로운 일에 착수하는 것보다는 관망하는 태도로 현상 유지에 힘써야 한다.
        정신수양이 안되면 변화에 적응하지 못해 심적으로 고통받게 된다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_20
    return


label g_121221(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}화뇌서합(火雷噬嗑){/b}{/size}

        {size=60}위는 불(火)이고 아래는 천둥 우레(雷)다.
        서합(噬嗑)에서 서(噬)는 씹다라는 뜻이고,
        합(嗑)은 입을 다물다라는 뜻이므로 ‘음식을 입안에 넣고 씹는다’는 의미다.
        불과 우레가 천지를 진동하니 위턱과 아래턱이 만나 입안의 음식물을 씹고 분쇄하여,
        나중에 하나로 화합한다는 뜻에서 서합(噬嗑)을 괘 이름으로 하였다.
        27번째 산뇌이(山雷頤) 괘가 있다.
        이(頤)는 턱이라는 뜻으로 위아래 두 양효(陽爻)는 위턱과 아래턱이고,
        음효(陰爻)는 턱 사이 이빨이 즐비한 형상이다.
        그런데 서합(噬嗑)을 위턱과 아래턱 사이에 하나의 양효가 있다.
        이는 입 속에 음식물이 있는 상태를 말한다.
        인간사에 있어서는 격렬한 언쟁과 싸움을 뜻하는 것으로 고난과 장애를 의미한다.
        이 괘를 얻은 사람은 격렬한 언쟁과 싸움에 휘말려 있고.
        서로 고집이 팽팽히 맞서 어느 쪽도 지지 않으려고 한다.
        어려움에 봉착해 있다.
        그러나 음식물을 다 씹어 삼키면 몸에 좋은 영양분이 되듯이
        싸움이 끝나면 전보다 더욱 다정해 진다.
        한 바탕 옥신각신은 필연적이니 차라리 멋지게 싸우고 기분 좋게 화해하는 것이 현명한 방법이다.
        힘에 겨운 일이나 주변 사람들과 불화가 있지만,
        용기를 잃지 않고 노력한다면 머지않아 기쁜 일이 있다.
        사업은 처음에는 어려움이 많겠지만,
        나중에는 크게 성공할 수 있으므로,
        새로운 사업을 벌이거나 사업 규모를 확장해도 좋다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_21
    return

label g_122121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}산화비(山火賁){/b}{/size}

        {size=60}위는 산(山)이고 아래는 불(火)이다.
        비(賁)는 ‘꾸미다’ ‘장식하다’라는 뜻이다.
        산아래 불이 있음은 해가 서산에 기울어 찬란한 황혼 노을을 나타내므로,
        아름답게 꾸민다는 뜻의 비(賁)를 괘의 이름으로 하였다.
        내적인 아름다움을 꾸민다는 뜻과 겉만 그럴 듯 하게,
        교언형색(巧言形色)으로 꾸민다는 뜻도 된다.
        내면의 세계에 충실한 사람은 매우 좋으나,
        그렇지 않은 사람에게는 허세를 부리거나 겉치레만 하다 실속이 없다.
        이 괘를 얻은 사람은 공연히 우쭐해지지 말고 분수에 맞는 생활을 하여야 한다.
        특히 남의 감언이설(甘言利說)이나 속임수 그리고 사기 등 금전상의 손실도 주의해야 한다.
        예술, 예능, 방송 등 화려한 일에 종사하는 사람은
        인기를 얻고 자신의 역량을 발휘할 수 있다.
        사업은 내실(內實)있는 경영을 하여야 한다. 괜히 허세를 부리다가는 실패한다.
        광고, 실내장식, 미용, 의상, 양화 등의 일에는 매우 좋은 괘다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_22
    return

label g_122222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}산지박(山地剝){/b}{/size}

        {size=60}위는 산(山)이고 아래는 땅(地)이다.
        박(剝)은 ‘벗기다’ ‘빼앗다’라는 뜻이다.
        산이 땅위에 우뚝 솟아 있으니 비바람에 깎여 벗겨지고,
        상처를 입는다는 뜻에서 박(剝)을 괘 이름으로 하였다.
        태산이 풍상(風霜)에 깎이어 점점 무너져 가는 상으로 매우 불길한 미래를 암시한다.
        한 개의 양이 다섯 개의 음 위에서 전전긍긍하는 모습이다.
        이 괘를 얻은 사람은 모든 운세가 급격히 쇠퇴해 가는 시기이므로 매사에 조심해야 한다.
        믿었던 사람에게 배신을 당하여 회복이 불가능한 피해를 당할 수 있다.
        인간의 힘으로 도저히 돌이킬 수 없는 쇠약한 운세이므로,
        경거망동하지 말고 조용히 자신을 지키며 이익보다는 소실을 막는 일을 생각해야 한다.
        모든 것이 붕괴되고 나면 새로운 창조가 시작되기 때문에,
        지금까지 고난의 연속이었던 사람은 곧 고난이 끝나고 새로운 전기가 마련된다.
        사업은 확장이나 신규 사업에 착수하지 말고 현상유지에 힘써야 한다.
        내부에서 분규가 일어나 어려움을 겪을 수 있으며,
        동업자나 신임하던 부하에게 배신당할 염려가 있다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_23
    return

label g_222221(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}지뇌복(地雷復){/b}{/size}

        {size=60}위는 땅(地)이고 아래는 우레 천둥(雷)이다.
        복(復)은 ‘돌아오다’ ‘회복하다’라는 뜻이다.
        땅 밑에서 천둥 우레가 울린다는 것은 땅위에 새로운 시작을 알리는 것과 같다.
        또 서서히 봄의 기운이 태동하고 있는 것과 같아 다시 시작한다는 뜻에서 복(復)을 괘 이름으로 하였다.
        여러 음 밑에서 하나의 양이 태동하고 있으니,
        산지박(山地剝) 괘와는 전연 반대의 상황이다.
        이 괘를 얻은 사람은 절망을 극복하고 새로운 희망으로 나가고 있다.
        곧 성공할 운을 맞고 있으니 묵은 감정을 버리고 새롭게 시작하라.
        무리하게 서둘지만 않는다면 반드시 성공한다.
        사업은 새로운 사업을 계획하는 것보다는,
        한번 실패했던 일을 다시 하거나 전에 하던 일을 하면 더욱 좋다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_24
    return

label g_111221(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}천뇌무망(天雷无妄){/b}{/size}

        {size=60}위는 하늘(天)이고 아래는 천둥 우레(雷)다.
        무(无)는 ‘없다’라는 뜻이고 망(妄)은 ‘허망하다’는 뜻이므로,
        욕망도 작위도 없는 자연 그대로의 순리를 나타내 무망(无妄)을 괘 이름으로 하였다.
        하늘에서 천둥 우레가 울리니 머지 않아 비가 올 것은 분명하지만,
        지금은 비가 올 듯 올 듯 하면서 오지 않고 있다.
        제일 아래에서 외롭게 움직이는 양의 기운을 위의 하늘이 돕고 있으니
        새로운 변화는 거스를 수 없는 대세다.
        이 괘를 얻은 사람은 진실하고 성의 있는 마음으로 시운(時運)에 순응해야 한다.
        얕은 지식이나 하찮은 경험으로 천명(天命)에 맞서는 것은 어리석다.
        현재 무언가를 갈구하지만 뜻대로 이루어지지 않아 고민과 불안에 빠져있다.
        초조하지 말고 침착하게 때를 기다리면 곧 좋은 일이 생긴다.
        사업은 애를 써도 이루어지지 않으니
        현상유지를 하면서 순리대로 일을 처리해야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_25
    return

label g_122111(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}산천대축(山川大畜){/b}{/size}

        {size=60}위는 산(山)이고 아래는 하늘(天)이다.
        대축(大畜)은 ‘크게 쌓다’ ‘많이 모이다’라는 뜻이다.
        하늘 위로 산 기운이 높이 솟아 오른 모습이니 새로운 변화가 하늘을 찌르고 있다.
        이러한 시기에 크게 축적이 되므로 대축(大畜)을 괘의 이름으로 하였다.
        농번기를 맞아 저수지에 물이 가득 차고 추수가 끝나 창고에 곡식이 가득 쌓인 것이므로,
        물질적으로 풍요로우며 정신적으로 안정된 상태다.
        이 괘를 얻은 사람은 어떠한 일에도 대길하다.
        본인의 역량도 뛰어날 뿐 아니라 시운이 매우 좋다.
        노력하는 대로 그에 비례하여 결실을 얻을 수 있다.
        포부를 크게 갖는 것이 좋다.
        사업은 무슨 일을 하든 비약적인 발전이 있으므로 적극적으로 나가는 것이 좋다.
        그러나 단숨에 일을 하려고 서두르면 안 된다.
        대축(大畜)에는 ‘머물다’ ‘기다리다’의 뜻도 있어
        큰일을 이루기 위해서 준비한다는 의미도 되기 때문이다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_26
    return

label g_122221(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}산뇌이(山雷頤){/b}{/size}

        {size=60}위는 산(山)이고 아래는 천둥 우레(雷)다.
        이(頤)는 ‘턱’ ‘기르다’ ‘봉양하다’의 뜻이다.
        산아래 천둥 우레가 진동하는 상이니 무언가 산 위로 올라가는 모습이므로,
        생명을 기른다는 의미의 이(頤)를 괘 이름으로 하였다.
        위아래는 양효(陽爻)로서 아래턱과 위턱을 나타내고
        가운데 음효(陰爻)들은 이빨이 가지런히 늘어선 형상을 하고 있다.
        입은 음식물을 씹어 영양분을 섭취하고 바른 언사로서 자신을 지키는 일을 한다.
        이 괘를 얻은 사람은 자기가 한말에 대해서 책임을 져야 하는 시점에 와 있다.
        책임지지 못할 말은 하지도 듣지도 않는 것이 좋다.
        머지않아 여러 사람의 협력을 얻어 자신의 뜻을 정력적으로 펴게 된다.
        사업은 음식물을 씹듯 차근차근 일을 추진하면 반드시 성공한다.
        처음에는 고난이 많고 이익이 적지만 나중에는 큰 이익을 얻을 수 있다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_27
    return

label g_211112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}택풍대과(澤風大過){/b}{/size}

        {size=60}위는 못(澤)이고 아래는 바람(風)이다.
        대과(大過)란 정상적인 괘도에서 크게 벗어나 ‘지나치다’라는 듯이다.
        잔잔한 못에 바람이 불어 물결이 크게 일어나니
        조그만 배가 망망대해에서 풍랑을 만난 상과 같아,
        지나치다라는 뜻에서 대과(大過)를 괘 이름으로 하였다.
        위아래 괘가 음효(陰爻)이고 가운데는 모두 양효(陽爻)이므로
        바닥과 위는 약한데 가운데가 강해 지탱할 수 없음을 나타낸다.
        예를 들어 임금의 세력이 약하고 아래 백성 또한 지쳐있는데,
        가운데 신하들이 권력을 강하게 마구 휘두르고 있으니 나라가 붕괴될 위험에 처해있는 상이다.
        이 괘를 얻은 사람은 모든 일에 크게 정도를 지나쳐 있다.
        또 진퇴양난에 빠져있다.
        지극히 비정상적인 상황에 있으면서도 자신은 그것을 깨닫지 못하고 있으니
        정신 차려 빨리 수습하지 않으면 큰 화를 입게 된다.
        대과(大過)란 ‘무거운 짐’이라는 뜻도 있으므로 잘못하면 과로에 쓰러지게 되므로
        포기할 일이라면 미련 없이 포기하는 것이 좋다.
        사업은 겉보기에는 화려해도 실속이 전혀 없으니 확장을 꾀할 때가 아니다.
        내실을 기하여 현상유지에 힘써야 한다.
        매우 불길한 괘이므로 대형사고 등에 조심해야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_28
    return

label g_212212(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}감위수(坎爲水){/b}{/size}

        {size=60}위도 물(水)이고 아래도 물(水)이다.
        물이 겹쳐 있으니 수(水)를 괘 이름으로 하였다.
        양효(陽爻)가 모두 두 음효(陰爻) 중간에 빠져있는 상이므로,
        빠진다 의미의 감(坎)이 거듭되어 감위수(坎爲水)라 하였다.
        세상의 모든 이치는 지나치면 위험에 빠지게 되어있다.
        이 괘를 얻은 사람은 악운의 소용돌이 속으로 빠져들고 있다.
        실패, 좌절, 파산, 병고 등의 어려운 일이 계속 발생한다.
        이러한 고통에서 벗어나려고 몸부림치면 칠수록 더 깊은 고통으로 빠져드니,
        비장한 각오로 배수진을 치고 힘껏 노력해야만 한다.
        철저한 자기 반성과 굳은 의지만이 난관을 타개하고 위험에서 벗어날 수 있다.
        사업은 대단히 불길한 조짐이 보이니 절대로 적극성을 취해서는 안 된다.
        최선의 노력을 했는데도 안될 때는 모든 것을 운명으로 생각하고,
        달관의 자세를 가지고 마음의 평정을 유지하는 것이 중요하다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_29
    return

label g_121121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}이위화(離爲火){/b}{/size}

        {size=60}위도 불(火)이고 아래도 불(火)이다.
        불 두 개가 겹쳐있으니 화(火)를 괘 이름으로 하였다.
        불 두 개는 태양을 상징하며 정열과 왕성한 의욕을 뜻하는 것이 이위화(離爲火)괘다.
        두 개의 음효(陰爻)가 상괘와 하괘 중앙에 자리잡고 있으면서
        왕성한 양기와 조화를 이루고 있다.
        이 괘를 얻은 사람은 대단한 성운(盛運)을 맞고 있으며
        명랑하고 유쾌한 반면 독단에 흐르기 쉬운 결점이 있다.
        결단과 박력이 있는 행동은 좋지만 과격한 행동 때문에 성운을 얻고도 일을 그르칠 수 있다.
        항상 중용(中庸)을 지키면서 신중하게 생각하고 행동한다면 크게 성공할 수 있다.
        사업은 매우 강한 운세여서 어려운 점이 없다.
        그러나 독불장군처럼 행동하지 말고 주위 사람들의 의견에 귀를 기울여야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_30
    return

label g_211122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}택산함(澤山咸){/b}{/size}

        {size=60}위는 못(澤)이고 아래는 산(山)이다.
        함(咸)은 감(感)과 같은 뜻으로 ‘느낌이 좋다’는 의미다.
        젊은 여자를 상징하는 태(兌)괘 아래 젊은 남자를 상징하는 간(艮)괘가 있으니,
        남녀간의 순수한 사랑을 느끼는 감상적인 의미의 함(咸)이다.
        이 괘를 얻은 사람은 이론과 논리를 따지는 것보다는,
        육감과 정감을 가지고 움직이면 남의 공감을 얻어 매사가 순조롭게 진행된다.
        무슨 일이나 바라는 대로 이루어지고 머지않아 뜻밖의 좋은 일이 일어난다.
        그러나 너무 감상적인 것에 사로잡혀 이성을 잃을 수가 있으므로
        연애 사건 등에 조심해야 한다.
        결혼에는 매우 좋은 괘다.
        사업은 관계자 모두가 일치 단결하여 주저하지 않고 밀고 나가면 성공할 수 있다.
        대인 관계에서 인간적인 면을 잃어서는 안 된다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_31
    return

label g_221112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}뇌풍항(雷風恒){/b}{/size}

        {size=60}위는 천둥 우레(雷)이고 아래는 바람(風)이다.
        항(恒)은 ‘변함이 없다’ ‘한결 같이 계속 된다’라는 뜻이다.
        상괘는 장남을 상징하는 진(震)괘이고 하괘는 장녀를 상징하는 손(巽)괘다.
        장남이 장녀 위에 있고 이들이 결혼 후에도 남편이 위에 있고 아내는 아래에 있으니,
        그 법도가 한결 같다는 뜻에서 항(恒)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 항상 한결 같은 마음으로 지금까지 지켜왔던 생활을 그대로 지켜 나가야 한다.
        비약적인 발전보다는 차근차근 내실을 기하면서 착실하게 성장해 나가는 것이 중요하다.
        사업은 확장이나 전업(轉業)은 좋지 않고 현상 유지에 만족해야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_32
    return

label g_111122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}천산둔(天山遯){/b}{/size}

        {size=60}위는 하늘(天)이고 아래는 산(山)이다.
        둔(遯)은 ‘피하다’ ‘물러나다’ ‘은둔하다’라는 뜻이다.
        산이 아무리 높다하더라도 하늘 아래 있고,
        밑에 있는 두 음효(陰爻)가 위에 있는 양효(陽爻)를 밀어내는 형상이니,
        이제 물러나라는 뜻에서 둔(遯)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 아무리 자신이 올바른 일을 해도 남들이 인정해주지 않고,
        오히려 시기와 모함을 받으므로 한 걸음 물러서 때를 기다리는 것이 좋다.
        지금 역경에 처해 있더라도 곧 역경에서 벗어날 수 있다.
        대체로 이 괘는 36계 줄행랑이 묘수다.
        사업은 전반적으로 침체가 되어 있으므로
        서두르지 말고 착실하게 내실을 기하는 것이 좋다.
        안될 일이라면 용단을 내려 
        미련 없이 손을 떼는 것이 오히려 이익일 수 있다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_33
    return

label g_221111(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}뇌천대장(雷天大壯){/b}{/size}

        {size=60}위는 천둥 우레(雷)이고 아래는 하늘(天)이다.
        대장(大壯)을 ‘힘차다’ ‘성대하다’ ‘씩씩하다’라는 뜻이다.
        하늘 위에서 우레가 움직이고 있고 아래에 있는 네 개의 왕성한 양이
        위에 있는 두 개의 음을 몰아 붙이고 있으므로,
        힘차고 씩씩하다는 뜻에서 대장(大壯)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 대단한 성운(盛運)으로
        매사에 의욕이 있고 체력도 강하여 적극적으로 일을 추진한다.
        그러나 의욕이 지나쳐 실패할 수도 있으므로 자신을 억제하는 것이 좋다.
        하나하나 차근차근 실속 있게 일을 추진하면 성공하는데,
        재주나 힘만 믿고 자만에 빠지거나 허세를 부리면 빈 수레가 요란하듯이 실속이 없다.
        사업은 허세를 부리지 않는다면 확장이나 신규 사업에 크게 성공할 수 있다.
        남의 부추김에 조심하고 항상 자기 분수를 알아야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_34
    return

label g_121222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}화지진(火地晉){/b}{/size}

        {size=60}위는 불(火)이고 아래는 땅(地)이다.
        진(晋)은 ‘나아가다’ 전진하다‘라는 뜻이다.
        불인 태양이 지상 위로 점점 떠오르면서 밝아지니
        나아간다는 의미에서 진(晋)을 괘 이름으로 하였다.
        태양이 높이 오를수록 어둠은 사라지고 천하가 밝아진다.
        이 괘를 얻은 사람은 운세가 서서히 강해지니 포부를 펼 때며 만사가 뜻대로 이루어진다.
        그러나 태양이 아무리 밝아도 구름에 가려져 
        그 위세를 잃을 수도 있으니 항상 성실하고 근면한 자세로 임해야 한다.
        주위에 질투, 시기, 모함 등이 많을 때이므로 
        넓은 아량과 용기로서 이러한 장애를 극복해야 한다.
        사업은 새로운 것에 착수할 좋은 기회다.
        경쟁이 심해도 성공할 수 있다.
        그러나 서서히 좋아지므로 서둘면 실패한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_35
    return

label g_222121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}지화명이(地火明夷){/b}{/size}

        {size=60}위는 땅(地)이고 아래는 불(火)이다.
        이(夷)는 상하고 깨지는 것이므로 명이(明夷)는 밝은 것이 상하고 깨진다는 뜻이다.
        태양이 땅 아래 지하에 잠겨가고 있으니
        어두움이 온다는 뜻에서 명이(明夷)를 괘 이름으로 하였다.
        이는 태양이 서산에 지는 상이다.
        이 괘를 얻은 사람은 매우 불길한 운세에 놓여 있다.
        자신의 지식이나 역량을 과신하여 섣불리 행동하면
        오히려 비방과 모함을 당하여 위험에 빠질 수 있다.
        밝은 낮의 선은 사라지고 어두운 밤의 악이 지배하는 시간이니
        모든 일에 손을 떼고 충분한 휴식을 취하는 것이 좋다.
        밤이 지나면 다시 밝은 내일이 온다.
        그때까지 내면의 실력을 쌓으며 참고 기다려야 한다.
        사업은 당분간 관망하는 것이 좋다.
        현상 유지도 힘들 때다.
        새로운 계획이 있더라도 기다렸다가 다시 생각해보아야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_36
    return

label g_112121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}풍화가인(風火家人){/b}{/size}

        {size=60}위는 바람(風)이고 아래는 불(火)이다.
        가인(家人)은 ‘집을 지키는 사람’을 뜻한다.
        상괘는 장녀(長女)를 상징하는 손(巽)괘이고 아래는 중녀(中女)를 뜻하는 이(離)괘다.
        동생이 언니 아래 있어 그 뜻을 따르니 
        일가(一家)가 편안히 다스려진다는 의미에서 가인(家人)을 괘 이름으로 하였다.
        집안이 평화롭기 위해서는 집을 지키는 부인이 순종하며 바른 도(道)를 지켜야 함을 나타낸 것이다.
        또 불 위에 바람이 불고 있으니 불씨를 꺼뜨리지 않고 잘 간수하는 것이
        옛 여자들의 중대사였고 집안을 다스리는 기본이었다.
        이 괘를 얻은 사람은 외부로 나서서 활동을 하는 것보다는
        차분하게 내부 일을 정비하는 것이 좋다.
        여자에게는 매우 좋은 괘로서 현모양처(賢母良妻)가 된다.
        항상 가족의 안위를 생각하고 따뜻한 마음을 지니도록 하는 것이 중요하다.
        사업은 확장보다는 현상 유지에 힘쓰는 것이 바람직하다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_37
    return

label g_121211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}화택규(火澤睽){/b}{/size}

        {size=60}위는 불(火)이고 아래는 못(澤)이다.
        규(睽)는 ‘서로 등지다’ ‘노려보다’ ‘사팔눈’이라는 뜻이다.
        불은 타오르면서 위로 올라가고 연못의 물은 낮은 쪽으로 흘러가니
        서로 등져 떨어지므로 규(睽)를 괘 이름으로 하였다.
        이 괘를 얻은 사람은 매사에 장애가 많고 다툼과 근심 속에서 지낸다.
        다른 사람과 전혀 의사가 통하지 않고 자신이 아무리 올바르게 행동하여도
        남들은 그것을 옮게 보아주지 않는다.
        누구에게도 도움을 받을 수 없어 소외감이 생겨 자포자기하기 쉽다.
        아무리 자신이 정당하더라도 싸우지 말고 화해하는 것이 좋으며 언행을 조심해야 한다.
        사업은 아무리 좋은 계획이더라도 지금 서둘러 추진하면
        내부에서 분쟁이 생기거나 사고가 나 실패하기 십상이다.
        겸허한 마음으로 자중하면서 고난의 때가 무사히 넘어가기를 기다려야 한다.
        전 임직원이 화합하여 일치 단결하는 것이 중요하다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_38
    return

label g_212122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}수산건(水山蹇){/b}{/size}

        {size=60}위는 물(水)이고 아래는 산(山)이다.
        건(蹇)은 ‘절뚝발이’ ‘나아가기 힘들다’ ‘멈추다’라는 뜻이다.
        산 위에 물이 있으니 산을 넘으면 다시 물이 앞길을 막고 있어 나아가기가 불편하니,
        절름발이라는 뜻을 가진 건(蹇)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 운세가 완전히 쇠운(衰運)으로 접어들고 있다.
        작은 산을 건너면 큰산이 기다리고, 작은 내를 건너면 큰 강이 앞을 가로막는다.
        험난한 일들을 많이 당한다.
        이 때는 부질없이 시간을 낭비하지 말고 수양과 사색에 힘쓰는 것이 현명하다.
        하던 일을 중지하고 잘못된 것을 찾아내는 것이 화를 최소화하는 방법이다.
        사업은 정리할 것은 정리하고 사업규모를 축소할 때다.
        사업 확장이나 신규 사업 참여는 반드시 실패한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_39
    return


label g_221212(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}뇌수해(雷水解){/b}{/size}

        {size=60}위는 천둥 우레(雷)이고 아래는 물(水)이다.
        해(解)는 ‘해결되다’ ‘해소된다’ ‘풀린다’라는 뜻이다.
        천둥 우레가 진동하여 비를 내리니 얼어붙었던 대지가 풀리는
        봄을 의미하므로 해(解)를 괘 이름으로 하였다.
        이 괘를 얻은 사람은 지금까지의 고난이 해소되므로
        모든 일이 술술 잘 풀려나가는 운세다.
        계획했던 사업이나 마음먹었던 일이 있으면 실천에 옮길 수 있는 좋은 기회다.
        해(解)는 문제 해결의 근본 원칙을 제시하고 있으므로,
        지난날 어려웠던 시절의 과실과 허물은
        서로 덮어주고 용서하는 것만이 화합으로 나가는 지름길이다.
        그러나 해(解)는 ‘쪼갠다’ ‘분해한다’라는 뜻도 있으므로
        지금까지의 상태가 무너져 파국에 이를 수도 있다.
        순조롭게 진행되어 왔던 일이라도
        방심하거나 노력을 게을리 하면 나쁜 결과를 초래할 수 있다.
        사업은 열심히 노력하면 모든 일이 순조롭게 풀린다.
        새로운 단합이 필요하고 공동 사업을 꾀하면 순조롭게 진행될 것이다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_40
    return

label g_122211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}산택손(山澤損){/b}{/size}

        {size=60}위는 산(山)이고 아래는 못(澤)이다.
        손(損)은 ‘덜다’ ‘줄이다’ ‘손해보다’라는 뜻이다.
        산 아래에 있는 저수지의 물은 들판을 적시기 위해,
        흘러가야 하므로 잃는다는 의미에서 손(損)을 괘의 이름으로 하였다.
        그러나 일반적으로 생각하는 잃거나 빼앗기는 손실과
        손해가 아니라 주는 희생을 말한다.
        따라서 아깝거나 애석하지 않고 오히려 보람을 느낀다.
        말하자면 가을의 풍성한 수확을 위해 투자를 해야 한다는 의미다.
        이 괘를 얻은 사람은 처음에는 어려운 일이 많으나,
        나중에는 자신이 기울인 노력의 몇 배 보람을 느낀다.
        따라서 눈앞의 작은 이익보다는 먼 장래를 생각하는 것이 좋다.
        지금 당장은 손해인 것 같으나 밝은 미래를 위해서는 과감한 투자가 필요하다.
        남을 위한 희생과 봉사는 뿌린 만큼 거둔다는 속담처럼 반드시 좋은 결과가 있다.
        사업은 무슨 일이든 꾸준히 노력하면 성공할 수 있으므로,
        현재 적자를 보고있더라도 장래성만 있다면 계속해도 좋다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_41
    return


label g_112221(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}풍뇌익(風雷益){/b}{/size}

        {size=60}위는 바람(風)이고 아래는 천둥 우레(雷)다.
        익(益)은 ‘더하다’ ‘증가하다’ ‘이익이다’라는 뜻이다.
        바람이 불고 천둥이 치니 비가 오며,
        비는 골고루 만물을 적셔 유익함을 주기 때문에 익(益)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 쇠운(衰運)에서 성운(盛運)으로,
        전진하는 강한 운세로 활력이 넘치며 몹시 바쁘다.
        지금까지 노력했던 일이 결실을 맺으니
        적극적으로 일을 추진하면 큰 이익을 얻을 수 있다.
        익(益)에는 공익(公益)의 뜻이 있다.
        눈앞에 보이는 자신의 이익보다는 먼 앞날의 모두를 위한 이익을 꾀하여야 한다.
        인정을 베풀거나 자선 사업에 투자하면 투자한 것 이상의 대가를 얻게 된다.
        사업은 무리만 하지 않는다면
        모든 일이 순조롭게 진행되어 성공할 수 있다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_42
    return


label g_211111(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}택천쾌(澤天夬){/b}{/size}

        {size=60}위는 못(澤)이고 아래는 하늘(天)이다.
        쾌(夬)는 ‘물리친다’ ‘결단한다’는 뜻이다.
        아래 다섯 양효(陽爻)가 위에 있는 하나의 음효(陰爻)를 밀어내고 있는 상이니
        쾌(夬)를 괘 이름으로 하였다.
        소인배인 음효 하나가 군자인 다섯 양효 위에 군림하고 있으니
        전체를 위해 소인을 물리칠 결단을 내릴 때다.
        또 하늘 위에 큰물이 있으니 홍수가 날 것이며 홍수는 만물을 휩쓸고 나간다.
        이 괘를 얻은 사람은 결단을 내릴 때다.
        우유부단한 마음은 중요한 일을 놓치기 쉽다.
        끊고 맺는 것을 확실히 하여 뒷날에 후회가 없도록 하여야 한다.
        인생에는 연습이 없다.
        순간 순간의 선택이 평생을 좌우하므로
        전체적인 합의하에 명분을 쌓고 일을 추진하면 반드시 성공한다.
        사업은 비록 위험이 따르더라도 결행할 일은 단호하게 결행해야 한다.
        미루다가는 후일에 큰 우환이 된다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_43
    return


label g_111112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}천풍구(天風姤){/b}{/size}

        {size=60}위는 하늘(天)이고 아래는 바람(風)이다.
        구(姤)을 ‘우연히 만나다’ ‘추하다’라는 뜻이다.
        하늘 아래에서 바람이 부니 
        흩어졌던 구름이 모이므로 만난다는 뜻의 구(姤)을 괘 이름으로 하였다.
        제일 아래의 하나의 음이 다섯 개의 양을 떠받치고 있으니,
        한 여자가 다섯 남자를 상대하는 창녀와 같다하여 추하다는 의미도 있다.
        이 괘를 얻은 사람은 좋은 일보다는 
        나쁜 일을 만날 가능성이 훨씬 크므로 모든 일에 장애가 많다.
        모든 일을 신뢰할만한 사람과 의논하여 처리하고 
        항상 자신의 위치와 분수를 지켜야 화를 면할 수 있다.
        특히 부정하고 기가 센 여자를 만나 뜻밖의 화를 당할 수 있으니 조심해야 한다.
        사업은 현재의 상태를 유지하는데 최선의 노력을 해야한다.
        함부로 다른 일을 하였다가는 크게 실패할 염려가 있다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_44
    return


label g_211222(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}택지췌(澤地萃){/b}{/size}

        {size=60}위는 못(澤)이고 아래는 땅(地)이다.
        췌(萃)을 ‘모인다’라는 뜻이다.
        땅위에 연못이 있으면 물이 모이니 모인다는 뜻의 췌(萃)을 괘 이름으로 하였다.
        물은 위에서 낮은 곳으로 흐르는 것이므로 위계질서와 예절을 나타내기도 한다.
        물이 모이듯 사람이 한곳으로 모이면 그만큼 재물도 한곳으로 많이 모인다.
        이 괘를 얻은 사람은 모든 일이 순조롭게 풀리므로 자신의 실력을 충분히 발휘할 때다.
        위 사람들의 의견을 따르면 후회할 일이 없다.
        주변에 사람이 많이 모이므로 유통되는 재물도 많아 날로 번창해 나간다.
        그러나 사람이 많으면 좋은 일도 많지만 나쁜 일도 많을 수 있다.
        다투지 않고 항상 화목을 유지하고 질서를 지키도록 해야 한다.
        사업은 풍부한 인적 자원을 최대한 활용하여 사세 확장을 꾀할 시기다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_45
    return

label g_222112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}지풍승(地風升){/b}{/size}

        {size=60}위는 땅(地)이고 아래는 바람(風)이다.
        승(升)을 ‘위로 상승하다’ ‘올라가다’ ‘번성하다’라는 뜻이다.
        땅 밑에 있는 바람이 위로 상승하고 있으니
        상승한다는 뜻의 승(升)을 괘 이름으로 하였다.
        역의 64괘 중 전진을 상징하는 괘는 3개다.
        화지진(火地晋)과 풍산점(風山漸) 그리고 지풍승(地風升)괘다.
        진(晋)괘는 욱일승천(旭日昇天)의 기세를 나타내지만 무언가 불안한 감이 있고,
        점(漸)괘는 안정된 발전은 하지만 발전 속도가 느리고 규모가 작다.
        승(升)괘는 이 두 괘의 장점만을 모아놓은 거와 같다.
        이 괘를 얻은 사람은 소질과 능력을 충분히 갖추고 있는 상태이므로
        머지않아 자신을 꽃피울 수 있다.
        왕성한 운세로 무엇을 하든 성공할 수 있는 괘다.
        그러나 급진적인 것은 좋지 않다.
        점차적으로 하나하나 전진해 나가야 하며 성급히 서두르면 실패한다.
        어떠한 일을 해도 성공할 수 있으므로
        새로운 일을 시작해도 좋고 현재하고 있는 일을 해도 좋다.
        너무 서두르지 않고 충분하게 
        내실을 다지면서 전진해 가면 반드시 성공한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_46
    return

label g_211212(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}택수곤(澤水困){/b}{/size}

        {size=60}위는 못(澤)이고 아래는 물(水)이다.
        곤(困)을 ‘부족하다’ ‘곤궁하다’ ‘괴롭다’ ‘통하지 않는다’라는 뜻이다.
        연못 아래에 있는 물이 빠지는 모습이니
        물이 부족한 대지의 만물이 곤궁에 처하게 되므로 곤(困)을 괘 이름으로 하였다.
        곤(困)이라는 글자도 나무가 울타리 안에 갇혀 뿌리를 뻗을 수 없으니,
        밖으로 성장할 수 없고 자유롭게 행동할 수 없는 곤궁의 의미를 뜻하고 있다.
        이 괘를 얻은 사람은 사방이 꽉 막힌 상태로
        생계조차도 어려울 정도로 극심한 곤궁에 처해있다.
        아무리 노력해도 성과가 없으니 힘만 들뿐이다.
        이럴 때일수록 현실을 직시하고 인내하며
        한 걸음 뒤로 물러서 다음 기회를 기다리는 것이 좋다.
        사업은 아무리 유망한 사업이라도 실천에 옮기면 실패하므로
        은인자중(隱忍自重,하면서 현상유지에 힘써야 한다.
        때를 기다리면 반드시 혼전될 때가 온다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_47
    return

label g_212112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}수풍정(水風井){/b}{/size}

        {size=60}위는 물(水)이고 아래는 바람(風)이다.
        정(井)을 ‘우물’ ‘두레박’을 뜻한다.
        바람이 물밑에 있는 것은 바람이 깊은 곳까지 통하는 모습이니
        우물을 뜻하는 정(井)을 괘 이름으로 하였다.
        우물물을 퍼 올리려면 두레박이 필요하고 노고가 필요하다.
        또한 우물물은 많은 생명들에게 혜택을 주는 것이다.
        이 괘를 얻은 사람은 노력과 의지가 필요하다.
        자신에게 아무리 훌륭한 능력이 있더라도 샘물을 퍼 올리려면 두레박이 필요하듯,
        자신의 의지와 노력이 없으면 아무 소용이 없다.
        우물물을 퍼 올리려면 두레박이 필요하듯 주변 사람과 합심하는 것이 중요하다.
        물을 퍼내면 처음에는 혼탁하더라도 다시 맑아지는 것처럼,
        처음에는 심적 불안과 갈등이 있으나 시간이 지나면 모두 해결된다.
        사업은 동업자끼리 분쟁이 생겨 어려우나 점차 서로 이해하게 된다.
        전업이나 확장보다는 현재의 상태를 유지하는 것이 좋다.
        우물은 퍼내도 다시 차지만 넘치지는 않는다.
        큰 욕심을 버려야 하고 남에게 베풀어야 한다.
        물이 고여 있으면 섞기 때문이다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_48
    return

label g_211121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}택화혁(澤火革){/b}{/size}

        {size=60}위는 못(澤)이고 아래는 불(火)이다.
        혁(革)을 ‘바꾸다’ ‘혁신하다’ ‘혁명’의 뜻이다.
        연못아래 불이 있으니 
        물이 끊어 증발하여 큰 변화를 하므로 혁(革)을 괘 이름으로 하였다.
        혁(革)을 짐승 가죽이라는 뜻으로 
        가죽의 털을 벗기면 전혀 다른 것으로 변하기 때문에 혁명이라는 의미가 있다.
        이 괘를 얻은 사람은 옛것을 버리고 새것을 취하려는 상으로서 
        커다란 변화의 조짐이 보이고 있다.
        잘못 된 것을 바로잡고 새로운 세계를 건설하는데 과감하게 나서야 한다.
        개혁은 신뢰성과 박력 그리고 결단성이 있어야 성공한다.
        용두사미(龍頭蛇尾,로 끝나서는 안되므로 지속적으로 진행해야 한다.
        사업은 매우 강한 운세이기 때문에 새로운 일이나 전업을 해도 좋다.
        종래의 방법을 바꾸면 좋은 결과를 얻을 수 있다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_49
    return

label g_121112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}화풍정(火風鼎){/b}{/size}

        {size=60}위는 불(火)이고 아래는 바람(風)이다. 
        정(鼎)을 ‘발이 셋인 솥’ ‘안정감’을 뜻한다.
        불 밑에 바람이 불고 있는 상이니 음식을 만들기 위해 아궁이에 불을 지피는 모습으로,
        음식을 만드는 솥을 뜻하는 정(鼎)을 괘 이름으로 하였다.
        솥은 세 개의 발이 달려 안정감이 있고 
        새로운 음식을 만드는 물건이니 안정되고 지속적인 혁신을 뜻하기도 한다.
        앞 괘 혁(革,에서 옛것을 제거하고 새롭게 바꾸었다면 
        이제 안정을 찾고 지속적인 혁신을 해나가야 한다.
        이 괘를 얻은 사람은 모든 면에서 안정되고 평온한 생활을 하게 된다.
        지속적인 안정을 위해서는 욕심을 버리고 주변 사람들과 화합해야한다.
        세 개가 일치해야 안정되지 하나만 어긋나도 기울어진다.
        공생(共生, 공존(共存) 공영(共榮)을 신조로 인화(人和)을 잘하고
        이익 분배에서도 공평해야 한다.
        사업은 초창기 혼란이 안정되어 가는 시점에 있다.
        주변 사람들과 일치 협력하여 일을 하면 크게 성공한다.
        그러나 화합이 안되면 크게 실패한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_50
    return

label g_221221(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}진위뇌(震爲雷){/b}{/size}

        {size=60}위도 천둥 우레(雷)이고 아래도 천둥 우레(雷)다.
        뇌(雷)을 ‘천둥 우레’ ‘몹시 두려워하다’ ‘사나운 모양’ ‘위엄을 떨치다’를 뜻한다.
        우레가 크게 진동하니 많은 사람들이 놀라 두려워하고 있다는 뜻에서 
        소성괘 이름 그대로 뇌(雷)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 새로운 변화를 예고하고 있으므로 항상 대처할 준비를 하고 있어야 한다.
        진(震)괘는 장남을 뜻하므로 집안의 어른으로서 명성을 얻거나 
        우두머리로서 중대한 결정을 내려야 할 때가 되었다.
        왕성한 활동력을 가지고 있고 어떠한 난관도 돌파할 수 있는 용기와 능력이 있으므로 
        무슨 일에나 성공할 수 있다.
        그러나 모든 일에 신중히 대처해야하므로 
        말을 삼가고 빈틈없는 계획과 침착성을 가져야 한다.
        사업은 한가지 일에만 총력을 기울인다면 놀라운 성공을 할 것이다.
        두 용이 구슬을 놓고 다투는 상이므로 매사에 경쟁이 심하다.
        너무 서둘거나 기분에 사로잡히면 실속을 얻지 못하니 내실을 기하여야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_51
    return

label g_122122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}간위산(艮爲山){/b}{/size}

        {size=60}위도 산(山)이고 아래도 산(山)이다. 
        산이 첩첩이 있으니 산(山)을 괘 이름으로 하였다.
        간(艮)괘는 하나의 양이 두 음 위에 있으니 
        그 이상 올라갈 수가 없어 그곳에 머무르고 있는 상이고,
        산은 움직이지 않고 그곳에 있으므로 ‘머무르다’라는 뜻이다.
        이 괘를 얻은 사람은 지금 난관에 봉착해 있다. 
        할 일은 태산같이 많은데 능력이 부족하므로,
        앞으로 나가는 것을 중지하고 힘을 길러야 한다.
        아무리 곤란한 처지에 있더라도 배신이나 변절을 하지 말고 
        굳은 신념을 갖고 지조를 지키면 곧 좋은 때가 온다.
        사업은 여러 가지 일에 손을 대면 실패하니 
        한가지 일에 전심전력하여야 한다.
        산 넘어 산이니 분수를 모르고 경거망동하면 안되고 
        산처럼 묵묵하게 꾸준히 노력하면 곧 그 산을 넘게 된다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_52
    return

label g_112122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}풍산점(風山漸){/b}{/size}

        {size=60}위는 바람(風)이고 아래는 산(山)이다. 
        점(漸)은 ‘점점’ ‘점차로 나아지는 것’을 뜻한다.
        산 위에 따뜻한 바람이 불어와 점차로 만물이 깨어나는 것을 상징하니,
        점차로 나아간다는 뜻의 점(漸)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 서서히 나아지는 것을 암시하고 있으니 
        인내심을 가지고 성실 근면하면 점진적으로 발전한다.
        비약적인 발전이나 허영을 꿈꾸지 말고 늦더라도 
        차근차근하게 일을 하는 것이 바람직하다.
        대기만사성(大器萬事成)이므로 아무리 큰 이익이 눈앞에 있더라도 
        순서와 절차를 지켜 나가야 된다.
        사업은 서서히 발전해 나가므로 서둘지 말고 투기 사업이나 지나친 확장을 하지 마라.
        크게 무리만 하지 않는다면 조금씩 만족스러운 성공을 해나갈 것이다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_53
    return

label g_221211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}뇌택귀매(雷澤歸妹){/b}{/size}

        {size=60}위는 천둥 우레(雷)이고 아래는 못(澤)이다. 
        귀매(歸妹)는 ‘정상적이지 못한 결혼’이라는 뜻이다.
        위는 나이든 남자를 상징하는 진(震)괘이고 아래는 어린 여자를 상징하는 손(巽)괘다.
        이는 젊은 여자가 중년 남자와 결혼하는 것으로 
        여자에게 음란한 소질이 있어 남자를 따라다니니,
        정상적이지 못하다는 뜻에서 귀매(歸妹)를 괘 이름으로 하였다.
        이 괘를 얻은 사람은 한순간의 잘못에 의해 
        두고두고 후회할 수 있으므로 시작을 잘해야 한다.
        처음에는 그럴 듯해도 끝이 나쁠 수 있으므로 매사에 신중하고 각별히 조심해야 한다.
        배우자의 선택을 잘못하여 일생을 망칠 수 있으므로 
        일시적인 감성에 치우치지 말고 냉철한 이성이 필요하다.
        사업은 한 발짝 뒤로 물러서 수동적인 태도를 취하고 남보다 앞장서지 말아야 한다.
        현상유지를 하는 것이 최선이므로 
        새로운 일이나 확장은 금물이다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_54
    return

label g_221121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}뇌화풍(雷火豊){/b}{/size}

        {size=60}위는 천둥 우레(雷)이고 아래는 불(火)이다. 
        풍(豊)은 ‘풍성하다’라는 뜻이다.
        천둥 우레가 치면서 비가 내린 후 햇볕이 밝게 빛나니 만물이 성장하여,
        풍성한 결실을 맺는다는 뜻에서 풍(豊)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 일생의 절정에 와 있어 매우 왕성한 운을 가지고 있다.
        노력한 만큼의 대가를 얻을 수 있으며 큰 결실을 위해서 더욱 더 노력해야 한다.
        그러나 풍성한 가을 뒤에는 추운 겨울이 오므로 
        점점 쇠운(衰運)이 도래하고 있음을 명심해야 한다.
        지금의 성운(盛運)을 유지하려면 겨울 준비를 하듯이 
        미래를 위한 준비를 철저히 해야 한다.
        사업은 지금이 절정이기 때문에 확장이나 
        신규 사업은 금물이고 오히려 조금씩 사업 규모를 줄여 내실을 기해야 한다.
        앞으로 다가올 혹독한 불황을 견디려면 
        불필요한 인원과 지출을 줄이고 저축을 해놓아야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_55
    return

label g_121122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}화산여(火山旅){/b}{/size}

        {size=60}위는 불(火)이고 아래는 산(山)이다.
        여(旅)을 ‘여행’ ‘집과 고향을 떠나 낯선 곳으로 가는 것’ 
        ‘방황하는 나그네’를 뜻한다.
        산 위에 태양이 있는데 산은 머물러 움직이지 않으므로 
        여관(旅館,과 같고, 불은 움직여 머무르지 않으므로,
        여행자와 같으므로 여(旅)을 괘 이름으로 하였다.
        또 태양이 산에서 떠서 산으로 지는 것은 
        나그네의 여정과 같으므로 여(旅)을 괘 이름으로 한 것이다.
        이 괘를 얻은 사람은 길고 긴 여정에 지칠 대로 지친 고통스러움에 처해있다.
        지금의 여행은 즐거운 것이지만 옛날의 여행은 고행이므로 
        모든 것이 불안정하고 고독과 번뇌가 끊이지 않는다.
        여행할 때는 의지할 사람이 아무도 없기 때문에 매우 우울하고 절망적이지만,
        대신 자신의 내면세계를 성장시킬 수 있는 좋은 기회다.
        참고 견디면 모든 것이 희망으로 돌아선다.
        대부분 새로운 환경에 처하게 되어 당황하는데 
        시간이 해결해주므로 때와 장소에 따라 잘 적응하도록 힘써야 한다.
        사업은 나아가기보다는 물러설 때다. 
        신규 사업에 손을 대거나 확장은 위험하다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_56
    return

label g_112112(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}손위풍(巽爲風){/b}{/size}

        {size=60}위도 바람(風)이고 아래도 바람(風)이다.
        위도 아래도 모두 바람이니 소성괘의 이름 그대로 풍(風)을 괘 이름으로 하였다.
        바람은 곧 공기이니 지상의 공간에 없는 곳이 없으나 실체를 눈으로 볼 수는 없다.
        손(巽)괘는 하나의 음이 두 양 아래에 있어 
        순종하고 따르는 형상이므로 유순하고 겸양의 의미가 있다.
        또 손풍(巽風)을 동남풍으로 부드러운 봄바람이다.
        이 괘를 얻은 사람은 겸손하고 진솔한 마음을 가져야 한다.
        그러나 본래 결단성이 부족하므로 일의 매듭을 짓지 못하게 된다.
        이 때문에 곤란한 일들을 많이 당해 심적으로 불안한 상태가 지속된다.
        봄바람은 환절기이므로 뜻밖의 불상사를 당하고 
        남의 감언이설(甘言利說)에 잘 속는 결점을 가지고 있다.
        스스로 자신의 결점을 알고 확고한 주관을 가지고 행동하여야 성공할 수 있다.
        사업은 모든 것이 부드럽게 해결되는 듯 하다가도 큰 고비를 맞을 수 있다.
        신규 사업을 벌여 확장하기보다는 지금까지 쌓아온 기반을 토대로 일부분 확장하는 것이 좋다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_57
    return

label g_211211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}태위택(兌爲澤){/b}{/size}

        {size=60}위도 못(澤)이고 아래도 못(澤)이다. 
        태(兌)을 ‘즐거움’ ‘온화한 분위기’를 뜻한다.
        위아래가 모두 연못이니 소성괘 이름 그대로 택(澤)을 괘 이름으로 하였다.
        태(兌)괘는 두 양이 아래에 있고 음이 위에 있어 부드러운 기쁨이 겉으로 나타나는 상이다.
        연못에 있는 물은 낮은 곳으로 흐르며 
        대지에 있는 모든 만물에게 골고루 물을 나누어주듯이,
        베푸는 곳에서 기쁨을 느낄 수 있다.
        이 괘를 얻은 사람은 입이 두 개 겹쳐있으니 
        남달리 뛰어난 화술(話術)을 구사한다.
        입은 화(禍)의 근원이기도 하므로 이 점을 조심해야 한다.
        겉보기에는 즐거운 같아도 내면으로는 괴로움을 겪고 있고,
        무익한 일로 바쁘고 무어라 단정 지을 수 없는 난처한 일에 봉착해 있다.
        파벌적인 대립이나 쟁론에 말려들지 않도록 조심해야 한다.
        연못 아래 연못은 바다로 지상의 모든 물들을 받아들이고 있는 상이므로,
        모든 사람들의 뜻을 받아들어 주는 것이 결국 이익이 된다.
        사업은 적극적으로 밀고 나갈 때가 아니므로 
        전진보다는 내실을 기하는 것이 좋다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_58
    return

label g_112212(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}풍수환(風水渙){/b}{/size}

        {size=60}위는 바람(風)이고 아래는 물(水)이다. 
        환(渙)을 ‘흩어지다’ ‘풀어지다’라는 뜻이다.
        물위에서 바람이 부니 물이 바람에 날려 사방으로 흩어지는 상이므로 
        환(渙)을 괘 이름으로 하였다.
        겨우내 열었던 물이 봄바람에 녹아 풀어지니 지금까지의 어려움이 모두 사라지고,
        밝고 희망찬 미래가 다가오고 있음을 암시한다.
        이 괘를 얻은 사람은 새로운 변화가 다가오고 있으니,
        그 동안 어려웠던 일들은 모두 털어 버리고 새로운 시작을 준비해야 한다.
        근심과 괴로움이 많았다면 그로부터 해방될 수 있는 시기다.
        이럴 때일수록 인화단결이 중요하므로 공동운명체라는 의식을 가져야 한다.
        사업은 순조롭게 진행되므로 무슨 일이든 적극성을 가지고 추진하면 성공한다.
        인간관계가 중요하니 인화(人和)에 힘써야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_59
    return

label g_212211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}수택절(水澤節){/b}{/size}

        {size=60}위는 물(水)이고 아래는 못(澤)이다. 
        절(節)을 ‘절도’ ‘규칙이나 제한’ ‘절약’을 뜻한다.
        연못 위에 물이 가득하니 물이 많으면 넘치게 하고,
        모자라면 흐르지 못하게 하니 절도를 뜻하는 절(節)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 절도 있는 생활을 하며 절약에 힘써야 한다.
        즐거움과 근심이 번갈아 생기므로,
        교만과 아집을 버리고 비굴할 정도의 아첨과 아부도 안되고,
        항상 중용(中庸)을 지키는 것이 중요하다.
        사업은 내실을 기하며 현상유지 한다는 자세로 일을 하면 
        착실하게 이익을 올릴 수 있다.
        큰 사업에 무리하게 뛰어든다면 맵새가 황새를 쫓아가는 꼴이 된다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_60
    return

label g_112211(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}풍택중부(風澤中孚){/b}{/size}

        {size=60}위는 바람(風)이고 아래는 연못(澤)이다.
        중부(中孚)는 ‘어미 새가 알을 품어 따뜻하게 한다’는 뜻이다.
        가운데 두 음효(陰爻)는 노른자이고 
        바깥 양효(陽爻)는 흰자와 껍데기를 나타내니 알의 모양을 뜻한다.
        또 왕성한 네 개의 양기가 중앙의 음기를 위아래에서 두텁게 호위하고 있으며,
        상괘와 하괘가 입을 맞춘 듯 대칭을 이루며 한 몸으로 결합되어,
        마치 어미 새가 알을 품고 있는 상이므로 중부(中孚)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 무슨 일이든 성공을 거둘 수 있는 상이다.
        자신의 능력도 있지만 주위에서 도와주는 사람이 많다.
        그러나 여러 사람의 도움에 우쭐하여 
        잘난 체하거나 나태해지면 당번에 나락(奈落,으로 떨어진다.
        사업은 비록 현재 부진한 상태에 있더라도 
        인내와 성의를 가지고 노력하면 머지 않아 성공한다.
        역량에 맞지 않는 일은 하지 말고 
        혼자보다는 주위의 도움을 받으면 더욱 좋다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_61
    return

label g_221122(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}뇌산소과(雷山小過){/b}{/size}

        {size=60}위는 천둥 우레(雷)이고 아래는 산(山)이다.
        소과(小過)을 ‘조금 지나치다’라는 뜻이다.
        상괘와 하괘가 등을 지고 있고 음이 양에 비해 약간 많다는 의미에서,
        조금 지나치다라는 뜻의 소과(小過)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 모든 일에 신중해야 하며 
        함부로 까불고 날뛰다가는 위험에 빠지게 된다.
        특히 대인 관계에 있어서 불상사가 많으므로 매사에 조심해야 한다.
        때에 따라서는 비굴하게 보일 만큼 저자세를 취하며 
        은인자중(隱忍自重)하는 것도 좋은 방법이다.
        사업은 신규 사업이나 확장을 꾀하는 것은 실패하여 패가망신할 수 있다.
        내부의 분규나 사고 등에 조심하고 규모를 줄여 내실을 기해야 한다.
        돌다리도 두들겨 보고 건너는 자세로 매사에 신중해야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_62
    return

label g_212121(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}수화기제(水火旣濟){/b}{/size}

        {size=60}위는 물(水)이고 아래는 불(火)이다.
        기제(旣濟,란 ‘일을 이미 성취했다’ ‘이미 물을 건넜다’ 
        ‘어려움에서 이미 벗어났다’라는 뜻이다.
        물은 위에 있고 불은 아래에 있으니 서로가 목적한 곳으로 건너가 있으므로,
        건넜다는 의미의 기제(旣濟)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 일생을 통하여 가장 왕성한 절정에 있는 운세로 
        더 이상 바랄 것이 없는 상태다.
        이제부터는 운세가 서서히 내리막길로 접어들기 때문에 현실에 안주하지 말고,
        확실한 기반을 다져 쇠퇴를 막고 
        지금의 성운(盛運)을 계속 누릴 수 있도록 해야 한다.
        사업은 현재는 좋은 상황이나 서서히 쇠퇴해가므로 
        내실을 기하고 규모를 줄여 다가올 불황에 대비해야 한다.{/size}
    """
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_63
    return

label g_121212(g__option=1):
    $ g_exp_messages = """
        {size=75}{b}화수미제(火水未濟){/b}{/size}

        {size=60}위는 불(火)이고 아래는 물(水)이다.
        미제(未濟)란 ‘미완성’을 뜻한다.
        불과 물이 각기 제자리에 있기 때문에 
        아직 건너지 않았다는 뜻에서 미제(未濟)을 괘 이름으로 하였다.
        이 괘를 얻은 사람은 지금까지의 모든 일이 미완성인체 이루어지지 않았음을 뜻하고 있으니,
        어그러지고 시의(時宜)에 맞지 않을 수 있다.
        현재는 매우 우울하고 절망적이지만 
        시간이 지나면 호전되므로 좌절하거나 포기하지 말아야 한다.
        겨울이 지나면 봄이 온다는 자연의 이치대로 
        그때를 대비하여 계획을 세우고 실력을 쌓아야 한다.
        사업은 내실을 기하면서 은인자중(隱忍自重)하고 있으면서 부단한 노력을 하여,
        현재의 어려운 상황을 극복하도록 노력해야 한다.
        곧 좋은 시기가 온다.{/size}
    """
    
    call display_bricks_message_v3(g_exp_messages) from _call_display_bricks_message_v3_64

    return
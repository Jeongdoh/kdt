#----------------------------------------------
library(shiny)

# ui 요소 구성 부분
ui<-fluidPage(
    # 웹페이지에 타이틀 ui 요소 추가
    titlePanel("데이터 분석"),

    # 웹페이지에 내용 ui 추가
    # 화면을 좌-우로 나누어서 사용 => sidebarLayout()
    sidebarLayout(
        # 좌 생성
        sidebarPanel(
            # 입력 ui
            radioButtons("type","Blood TYPE", c("A","B","AB","O")),
            sliderInput("age","AGE", min = 0,max = 200,value = 20)
        ),

        # 우 생성
        mainPanel(
            # 출력 ui
            # blood type을 텍스트로 출력
            textOutput("blood"),
            # Age에 대한 그래프 출력
            plotOutput("pAge")
        )     
    )
)


# server 구현 부분
server<-function(input, output, session){
    # input 매개변수 <= ui로 부터 입력받은 데이터가 저장되어있음
    # ex) input$type, input$age

    # 출력 ui에 데이터 렌더링하기(구현하기)
    # output$blood, output$Age
    output$blood<-renderText(paste("당신의 혈액형은", input$type , "형 입니다."))
    output$pAge<-renderPlot(plot(0:input$age,col='red', pch=20))
}

ui<-fluidPage(
    # 웹 페이지에 타이틀 ui요소 추가
    titlePanel("다이아몬드 데이터 분석"),

    # 웹 페이지에 내용 ui요소 추가
    tabsetPanel(
        tabPanel("캐럿"),
        tabPanel("투명도"),
        tabPanel("컷팅")
    )
)







# shiny app 실행부분
shinyApp(ui, server)







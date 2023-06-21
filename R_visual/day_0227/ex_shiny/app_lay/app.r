library(shiny)

ui<-fluidPage(
    titlePanel("다이아몬드 투명도에 따른 분석"),
    sidebarLayout(
        sidebarPanel(
            sliderInput("level","Diamond level",min=0,max=10,value=3)
        ),
        mainPanel(
            textOutput("selectValue")
        ),
    )
)

# server => ui 요소에 데이터 생성 및 입력처리
server<-function(input,output,session){
    output$selectValue<-renderText(input$level)
}

shinyApp(ui,server)
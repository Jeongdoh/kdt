library(shiny)

# UI
ui <- fluidPage(
  titlePanel("췌장암과 당뇨병의 상관계수 및 회귀분석 결과"),
  
  sidebarLayout(
    sidebarPanel(
      h4("데이터셋 선택"),
      selectInput("dataset", "데이터셋", 
                  choices = c("남성", "여성"), 
                  selected = "남성"),
      
      h4("나이 선택"),
      sliderInput("age", "나이", 
                  min = 20, max = 70, value = 20, step = 10),
      
      actionButton("correlation", "상관계수 구하기"),
      actionButton("regression", "회귀분석 결과 구하기")
    ),
    
    mainPanel(
      h4("결과 출력"),
      textOutput("result")
    )
  )
)

# 서버
server <- function(input, output) {
  data <- reactive({
    if (input$dataset == "남성") {
      file <- "cancer_man.csv"
    } else {
      file <- "cancer_woman.csv"
    }
    read.csv(file)
  })
  
  correlation <- eventReactive(input$correlation, {
    col_x <- paste0("X2.", as.integer((input$age-1)/10)+1)
    col_y <- paste0("X3.", as.integer((input$age-1)/10)+1)
    cor(data()[, col_x], data()[, col_y])
  })
  
  regression <- eventReactive(input$regression, {
    col_x <- paste0("X2.", as.integer((input$age-1)/10)+1)
    col_y <- paste0("X3.", as.integer((input$age-1)/10)+1)
    lm(data()[, col_x] ~ data()[, col_y])
  })
  
  output$result <- eventReactive(list(input$correlation, input$regression), {
    if (input$correlation) {
      paste0("상관계수: ", round(correlation(), 2))
    } else if (input$regression) {
      summary(regression())$coefficients
    } else {
      ""
    }
  })
}

# 런
shinyApp(ui = ui, server = server)

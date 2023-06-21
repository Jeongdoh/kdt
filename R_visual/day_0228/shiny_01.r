library(shiny)
library(ggplot2)

cancer_M_df <- read.csv("cancer_man.csv")
cancer_W_df <- read.csv("cancer_woman.csv")

ui <- fluidPage(
  titlePanel("췌장암과 당뇨병의 상관계수와 회귀분석"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("gender", "성별", choices = c("남자", "여자")),
      sliderInput("age", "나이(세)", min = 20, max = 70, value = 20, step = 10)
    ),
    
    mainPanel(
      plotOutput("correlation_plot"),
      plotOutput("regression_plot")
    )
  )
)

server <- function(input, output) {
  gender_data <- reactive({
    if(input$gender == "남자") {
      gender_df <- cancer_M_df
    } else {
      gender_df <- cancer_W_df
    }
    
    selected_df <- gender_df[, c(input$age/10*2+1, input$age/10*2+2)]
    names(selected_df) <- c("췌장암", "당뇨병")
    selected_df
  })
  
  output$correlation_plot <- renderPlot({
    cor_plot <- ggplot(gender_data(), aes(x = 췌장암, y = 당뇨병)) + 
      geom_point(size = 3) +
      labs(title = "췌장암과 당뇨병 상관그래프", x = "췌장암", y = "당뇨병") +
      theme_bw()
    cor_plot
  })
  
  output$regression_plot <- renderPlot({
    regression_model <- lm(췌장암 ~ 당뇨병, data = gender_data())
    regression_plot <- ggplot(gender_data(), aes(x = 당뇨병, y = 췌장암)) + 
      geom_point(size = 3) +
      geom_smooth(method = "lm", formula = y ~ x, color = "red") +
      labs(title = "췌장암과 당뇨병 회귀그래프", x = "당뇨병", y = "췌장암") +
      theme_bw()
    regression_plot
  })
}

shinyApp(ui = ui, server = server)























# library(shiny)
# library(ggplot2)

# # 데이터 로드
# cancer_M_df <- read.csv("cancer_man.csv")
# cancer_W_df <- read.csv("cancer_woman.csv")

# # UI 부분
# ui <- fluidPage(
#   # 타이틀
#   titlePanel("20대~70대 남녀별 췌장암과 당뇨병 상관분석 및 회귀분석"),
  
#   # 20대 남녀별 췌장암과 당뇨병 상관계수 그래프
#   sidebarLayout(
#     sidebarPanel(
#       h3("20대 남녀별 췌장암과 당뇨병 상관계수"),
#       verbatimTextOutput("correlation_20s")
#     ),
#     mainPanel(
#       h4("20대 남녀별 췌장암과 당뇨병 상관계수 그래프"),
#       plotOutput("scatterplot_20s")
#     )
#   ),
  
#   # 20대 남녀별 췌장암과 당뇨병 회귀분석 결과
#   fluidRow(
#     column(6,
#            h3("20대 남초록색, 여분홍색 췌장암과 당뇨병 회귀분석 결과"),
#            verbatimTextOutput("regression_20s")
#     ),
#     column(6,
#            h4("20대 남녀별 췌장암과 당뇨병 회귀분석 그래프"),
#            plotOutput("regressionplot_20s")
#     )
#   ),
  
#   # 30대 남녀별 췌장암과 당뇨병 회귀분석 결과
#   fluidRow(
#     column(6,
#            h3("30대 남초록색, 여분홍색 췌장암과 당뇨병 회귀분석 결과"),
#            verbatimTextOutput("regression_30s")
#     ),
#     column(6,
#            h4("30대 남녀별 췌장암과 당뇨병 회귀분석 그래프"),
#            plotOutput("regressionplot_30s")
#     )
#   ),
  
#   # 40대 남녀별 췌장암과 당뇨병 회귀분석 결과
#   fluidRow(
#     column(6,
#            h3("40대 남초록색, 여분홍색 췌장암과 당뇨병 회귀분석 결과"),
#            verbatimTextOutput("regression_40s")
#     ),
#     column(6,
#            h4("40대 남녀별 췌장암과 당뇨병 회귀분석 그래프"),
#            plotOutput("regressionplot_40s")
#     )
#   ),
#   # 50대 남녀별 췌장암과 당뇨병 회귀분석 결과
#   fluidRow(
#     column(6,
#            h3("50대 남초록색, 여분홍색 췌장암과 당뇨병 회귀분석 결과"),
#            verbatimTextOutput("regression_50s")
#     ),
#     column(6,
#            h4("50대 남녀별 췌장암과 당뇨병 회귀분석 그래프"),
#            plotOutput("regressionplot_50s")
#     )
#   ),
#   # 60대 남녀별 췌장암과 당뇨병 회귀분석 결과
#   fluidRow(
#     column(6,
#            h3("60대 남초록색, 여분홍색 췌장암과 당뇨병 회귀분석 결과"),
#            verbatimTextOutput("regression_60s")
#     ),
#     column(6,
#            h4("60대 남녀별 췌장암과 당뇨병 회귀분석 그래프"),
#            plotOutput("regressionplot_60s")
#     )
#   ),
#   # 70대 남녀별 췌장암과 당뇨병 회귀분석 결과
#   fluidRow(
#     column(6,
#            h3("70대 남초록색, 여분홍색 췌장암과 당뇨병 회귀분석 결과"),
#            verbatimTextOutput("regression_70s")
#     ),
#     column(6,
#            h4("70대 남녀별 췌장암과 당뇨병 회귀분석 그래프"),
#            plotOutput("regressionplot_70s")
#     )
#   ),
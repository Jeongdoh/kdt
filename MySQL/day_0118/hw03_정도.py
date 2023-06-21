import pymysql
import pandas as pd

# user 테이블 만들기
def user_table(conn, cur):
    try:
        query="""
        create table user_table
        (userID CHAR(8) not null primary key,
        userName varchar(10) not null,
        birthYear int not null,
        addr char(2) not null,
        mobile1 char(3),
        mobile2 char(8),
        height smallint,
        mDate date)
        """
        cur.execute(query)
        conn.comit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)



# user_table 값 입력
def user_insert(conn,cur):
    try:
        sql = """insert	into user_table(userID, userName, birthYear, addr, mobile1, mobile2, height, mDate)
        values (%s, %s, %s, %s, %s, %s, %s, %s)"""

        data=(('KHD','강호동',1970,'경북','011','22222222',182,'2007-07-07'),
                ('KJD','김제동',1974,'경남','','',173,'2013-03-03'),
                ('KKJ','김국진',1965,'서울','019','33333333',171,'2009-09-09'),
                ('KYM','김용만',1967,'서울','010','44444444',177,'2015-05-05'),
                ('LHJ','이휘재',1972,'경기','011','88888888',180,'2006-04-04'),
                ('LKK','이경규',1960,'경남','018','99999999',170,'2004-12-12'),
                ('NHS','남희석',1971,'충남','016','66666666',180,'2017-04-04'),
                ('PSH','박수홍',1970,'서울','010','00000000',183,'2012-05-05'),
                ('SDY','신동엽',1971,'경기','','',176,'2008-10-10'),
                ('YJS','유재석',1972,'서울','010','11111111',178,'2008-08-08'))

        cur.executemany(sql, data)
        conn.commit()
        print('INSERT 완료')
    except Exception as e:
        print(e)


# buy테이블 만들기
def buy_table(conn, cur):
    try:
        query="""
        create table buy_table
        (num INT auto_increment not null primary key,
        userID CHAR(8) not null,
        prodName CHAR(6) not null,
        groupName CHAR(4),
        price INT not null,
        amount SMALLINT not	null)
        """
        cur.execute(query)
        conn.comit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)


# buy테이블 값 입력
def buy_insert(conn, cur):
    try:
        sql = """insert	into buy_table(num, userID, prodName, groupName, price, amount)
        values (%s, %s, %s, %s, %s, %s)"""

        data=((1,'KHD','운동화','',30,2),
                (2,'KHD','노트북','전자',1000,1),
                (3,'KYM','모니터','전자',200,1),
                (4,'PSH','모니터','전자',200,5),
                (5,'KHD','청바지','의류',50,3),
                (6,'PSH','메모리','전자',80,10),
                (7,'KJD','책','서적',15,5),
                (8,'LHJ','책','서적',15,2),
                (9,'LHJ','청바지','의류',50,1),
                (10,'PSH','운동화','',30,2),
                (11,'LHJ','책','서적',15,1),
                (12,'PSH','운동화','',30,2))

        cur.executemany(sql, data)
        conn.commit()
        print('INSERT 완료')
    except Exception as e:
        print(e)



# 조인테이블 만듦
def join_table(conn, cur):
    try:
        query="""
        select userName, prodName, addr,
        concat(u.mobile1,u.mobile2) as '연락처'
        from user_table as u inner join buy_table as b
        on b.userID = u.userID;
        """
        cur.execute(query)
        data=cur.fetchall()
        data=pd.DataFrame(data)
        print(data)
    except Exception as e:
        print(e)


#kym 구매목록 찾기
def kym_buy(conn, cur):
    try:
        query="""
        select u.userID, u.userName, b.prodName, u.addr,
        concat(u.mobile1,u.mobile2) as '연락처'
        from user_table as u inner join buy_table as b
        on b.userID = u.userID
        where u.userID='KYM';
        """
        cur.execute(query)
        data=cur.fetchall()
        data=pd.DataFrame(data)
        print(data)
    except Exception as e:
        print(e)


# 전체회원 구매목록을 회원 아이디 순으로 정렬
def all_buy(conn, cur):
    try:
        query="""
        select u.userID, u.userName, b.prodName, u.addr,
        concat(u.mobile1,u.mobile2) as '연락처'
        from user_table as u inner join buy_table as b
        on b.userID = u.userID
        order by u.userID;
        """
        cur.execute(query)
        data=cur.fetchall()
        data=pd.DataFrame(data)
        print(data)
    except Exception as e:
        print(e)



#쇼핑몰에서 한번이라도 구매한 기록이 있는 회원 정보를 회원 아이디 순 출력
def maybe_one(conn, cur):
    try:
        query="""
        select distinct u.userID, u.userName, u.addr
        from user_table as u inner join buy_table as b
        on b.userID = u.userID
        order by u.userID;
        """
        cur.execute(query)
        data=cur.fetchall()
        data=pd.DataFrame(data)
        print(data)
    except Exception as e:
        print(e)


#경북, 경남인 회원 정보 출력
def gyeong_sang(conn, cur):
    try:
        query="""
        select u.userID, u.userName, u.addr,
        concat(u.mobile1,u.mobile2) as '연락처'
        from user_table as u inner join buy_table as b
        on b.userID = u.userID
        where u.addr in ('경북','경남');
        """
        cur.execute(query)
        data=cur.fetchall()
        data=pd.DataFrame(data)
        print(data)
    except Exception as e:
        print(e)

def main():
    #	데이터베이스(sqlclass_db)	연결
    conn = pymysql.connect(host='localhost', user='root',	password='coowjdeh14',
                                db ='shoppingmall', charset='utf8')
    # cursor 객체 생성
    cur = conn.cursor()
    #	테이블 생성 함수 호출
    user_table(conn, cur)
    user_insert(conn,cur)
    buy_table(conn, cur)
    buy_insert(conn, cur)
    join_table(conn, cur)
    kym_buy(conn, cur)
    all_buy(conn, cur)
    maybe_one(conn, cur)
    gyeong_sang(conn, cur)
    #	연결 종료
    cur.close()
    conn.close()
    print('Database	연결 종료')
main()




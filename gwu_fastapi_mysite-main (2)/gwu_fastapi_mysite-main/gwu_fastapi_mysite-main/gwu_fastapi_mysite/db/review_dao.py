from gwu_fastapi_mysite-main.gwu_fastapi_mysite-main.gwu_fastapi_mysite.db.common.connection import connection

# 다음 영화 리뷰 저장(리뷰, 평점, 작성자, 작성일자)
def add_review(data):
    # 1.Connection
    conn = connection()

    try:
        curs = conn.cursor()
        sql = f"""
                CREATE TABLE `test` (
	`no` INT(10) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_general_ci',
	`review` VARCHAR(500) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`score` INT(10) NOT NULL DEFAULT '0',
	`writer` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`reg_date` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`no`) USING BTREE
)
COMMENT='다음 영화 리뷰'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=1
;
              """
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        conn.close()
## /wxbot
```text
暂无描述
```
#### 公共Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /wxbot/用户
```text
暂无描述
```
#### 公共Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /wxbot/用户/删除
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/users/delete

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
    "username": "mike",
    "password": "mike99"
}
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"message": "删除成功"
}
```
#### 错误响应示例
```javascript
{
	"message": "密码错误，删除失败"
}
```
## /wxbot/用户/注册
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/users/register

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
    "username": "root",
    "password": "admin"
}
```
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
username | - | String | 是 | 用户名
password | - | String | 是 | 密码
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"message": "登录成功"
}
```
参数名 | 示例值 | 参数类型 | 参数描述
--- | --- | --- | ---
message | - | String | 
#### 错误响应示例
```javascript
{
	"message": "登录失败"
}
```
## /wxbot/用户/登录
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/users/login

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
    "username": "fanyq",
    "password": "admin"
}
```
参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述
--- | --- | --- | --- | ---
usename | - | String | 是 | 用户名
password | - | String | 是 | 密码
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"message": "登录成功",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTY2NDUzNDcsImlhdCI6MTY1NjY0MTc0NywidXNlcm5hbWUiOiJyb290In0.mn95vmdKLRpiTCp2dQz_NsLuZB0hJHSjPSZ_j0Goawk"
}
```
#### 错误响应示例
```javascript
{
	"message": "登录失败"
}
```
## /wxbot/用户/修改密码
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/users/update

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
    "username": "mike",
    "old_password": "admin",
    "new_password": "mike99"
}
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"message": "修改成功"
}
```
#### 错误响应示例
```javascript
{
	"message": "密码错误，修改失败"
}
```
## /wxbot/主页
```text
暂无描述
```
#### 公共Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /wxbot/主页/验证token
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/helloworld

#### 请求方式
> GET

#### Content-Type
> json

#### 请求Body参数
```javascript
{
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTY2NDkwNzMsImlhdCI6MTY1NjY0NTQ3MywidXNlcm5hbWUiOiJyb290In0.eGPykcXV1gC9C0DmCYyyeX0efCrv5s1fLRi3gNBYfsY"
}
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"message": "Hello World"
}
```
## /wxbot/消息
```text
暂无描述
```
#### 公共Header参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Query参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 公共Body参数
参数名 | 示例值 | 参数描述
--- | --- | ---
暂无参数
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
## /wxbot/消息/修改消息
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/message/update

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
	"keyword": "name",
	"message": "my name is mike",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTY2OTUxNDIsImlhdCI6MTY1NjY1OTE0MiwidXNlcm5hbWUiOiJmYW55cSJ9.I4sxk7vAPdtd4mKoWxu8ghPIDvhuw8zA2u-G-D5mw1c"
}
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": 200,
	"msg": "update mesage sucess"
}
```
## /wxbot/消息/添加消息
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/message/add

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
	"keyword": "name",
	"message": "my name is mike",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTY2OTUxNDIsImlhdCI6MTY1NjY1OTE0MiwidXNlcm5hbWUiOiJmYW55cSJ9.I4sxk7vAPdtd4mKoWxu8ghPIDvhuw8zA2u-G-D5mw1c"
}
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 错误响应示例
```javascript
{
	"message": "keyword is exist"
}
```
## /wxbot/消息/查询消息
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/message/query

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
	"keyword": "",
	"message": "",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTY2OTUxNDIsImlhdCI6MTY1NjY1OTE0MiwidXNlcm5hbWUiOiJmYW55cSJ9.I4sxk7vAPdtd4mKoWxu8ghPIDvhuw8zA2u-G-D5mw1c"
}
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
[
	{
		"id": 1,
		"username": "root",
		"keyword": "test",
		"message": "test"
	},
	{
		"id": 2,
		"username": "root",
		"keyword": "h",
		"message": "test"
	}
]
```
## /wxbot/消息/删除消息
```text
暂无描述
```
#### 接口状态
> 已完成

#### 接口URL
> http://10.249.2.7/message/del

#### 请求方式
> POST

#### Content-Type
> json

#### 请求Body参数
```javascript
{
	"message": "",
	"keyword": "name",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTY2OTUxNDIsImlhdCI6MTY1NjY1OTE0MiwidXNlcm5hbWUiOiJmYW55cSJ9.I4sxk7vAPdtd4mKoWxu8ghPIDvhuw8zA2u-G-D5mw1c"
}
```
#### 预执行脚本
```javascript
暂无预执行脚本
```
#### 后执行脚本
```javascript
暂无后执行脚本
```
#### 成功响应示例
```javascript
{
	"code": 200,
	"msg": "delete success"
}
```
#### 错误响应示例
```javascript
{
	"code": 400,
	"msg": "delete failed"
}
```
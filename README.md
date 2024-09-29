# 一个权限控制联系项目 心血来潮写一写
根据item划分权限  
基于django自带权限的权限控制  
django3  
vue2  
# 权限管理
权限 -> 角色(组) -> 用户  

<img width="1512" alt="image" src="https://user-images.githubusercontent.com/39042836/203276504-fd5b8805-5d58-43ad-a929-6dffcd511b41.png">
<img width="1512" alt="image" src="https://user-images.githubusercontent.com/39042836/203276609-3ce1d560-d803-4497-8020-bb58a73672ec.png">


## 权限说明：
|权限|说明|
| :----  | :----  |
|user add| 创建用户 |
|user change| 可以给用户分配角色(组)，修改用户信息|
|user view| 查看用户列表|
|user delete| 奥|
|group add|创建角色(组)|
|group change| 修改角色信息(组)|
|group view|查看角色列表(组)|
|group delete|奥|
|permission view|可以查看和分配角色(组)权限|
|items add|添加项目权限|
|items change|修改项目管理权限|
|items view|查看项目管理权限|
|items delete|奥|
|items view 项目名|可以查看与此项目关联的所有(不包含items的管理)|
|view_itemplans|查看项目详情,配合"items view 项目名"即可查看特定授权项目详情|



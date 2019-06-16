#创建字典
adress = {
    'Tom':{
        'name':'Tom',
        'tel':'13333333333',
        'email':'13333333333@qq.com',
        'company':'baidu'
    },
    'Joe':{
        'name':'Joe',
        'tel':'15555555555',
        'email':'15555555555@qq.com',
        'company':'ali'
    }
}
#删除通讯人
adress.pop('Tom')
print('删除Tom后',adress)
#增加通讯人
name=input('通讯人的名字:')
tel=input('通讯人的电话:')
email=input('通讯人的email:')
company=input('通讯人的公司:')
# adress[name]['name']=name  
# adress[name]['tel']=tel
# adress[name]['email']=email
# adress[name]['company']=company
adress.setdefault(name,{'name':name,'tel':tel,'email':email,'company':company})
print('增加{}之后:\n'.format(name),adress)

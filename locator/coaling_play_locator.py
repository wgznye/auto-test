

class CoalingPlayLocator:
    station_tab_loc = "//li[contains(text(),' 物流仓储中心 ')]"
    create_coaling_loc = "//span[contains(text(),'创建上煤计划')]"
    not_link_loc = "//span[contains(text(),'暂不关联')]"
    forwarding_unit_loc = "//div[contains(text(),'请选择发货单位')]"
    forwarding_unit_select_loc = "//li[contains(text(),'天宇源')]"
    receiving_unit_loc = "//div[contains(text(),'请选择收货单位')]"
    receiving_unit_select_loc = "//li[contains(text(),'河南荣厚')]"
    coal_loc = "//div[contains(text(),'请选择煤种')]"
    coal_select_loc = "//li[contains(text(),'123')]"
    warehouse_loc = "//div[contains(text(),'请选择仓房')]"
    warehouse_select_loc = "//li[contains(text(),'1号堆煤区')]"
    goods_allocation_loc = "//div[contains(text(),'请选择货位')]"
    goods_allocation_select_loc = "//li[contains(text(),'货位2')]"
    forwarding_station_loc = '//input[@placeholder="请输入发站"]'
    plan_wright_loc = '//input[@placeholder="请输入计划吨数"]'
    description_loc = '//textarea[@placeholder="请输入内容描述"]'
    submit_loc = "//span[contains(text(),'提 交')]"


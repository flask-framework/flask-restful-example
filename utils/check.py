def check_unique_field_exit(model, field_name, value):
    """
    校验唯一字段值是否存在
    :param model: [Model] 表结构model类
    :param field_name: [str] 字段名称
    :param value: [str] 值
    :return: [boolean] True: 存在, False: 不存在
    """
    unique_field = getattr(model, field_name)
    obj = model.query.filter_by(unique_field == value).first()
    if obj is None:
        return False
    return True

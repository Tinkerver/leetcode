# 简单加法
self.tik_instance.vec_add(self.input_num,
                          self.input_x_ub[0],
                          self.input_x_ub[0],
                          self.input_y_ub[0],
                          1, 8, 8, 8)

# repeat多次重叠
self.tik_instance.vec_add(self.input_num,
                          self.input_x_ub[0],
                          self.input_y_ub[0],
                          self.input_x_ub[0],
                          255, 0, 0, 0)

# range多次重叠
with self.tik_instance.for_range(0,100) as i:
    self.tik_instance.vec_add(self.input_num,
                              self.input_x_ub[0],
                              self.input_y_ub[0],
                              self.input_x_ub[0],
                              255, 0, 0, 0)

# unified buffer赋值
self.tik_instance.vec_dup(128, dst_ub, src_scalar, 1, 8)

# global memory 与unified buffer数据搬运
with self.tik_instance.for_range(0,100) as i:
self.tik_instan6ce.data_move(self.input_y_ub,
                            self.input_y_gm, 0, 1,
                            self.input_num // 16, 0, 0)

# unified buffer中跨地址访问速度
with self.tik_instance.for_range(0,255) as i:
    t=i+stride
    if t>=255:
        t%=stride
    self.input_x_ub[i]=(int)self.input_y_ub+2*t

#新建一个buffer，大小为128kb
#跨步访问
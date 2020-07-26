# helen-
helen数据集处理，多进程加速处理

# 原图
![原图](https://github.com/yuguolong/helen-data-processing/blob/master/jpg/232194_1.jpg)

# 标签
![标签](https://github.com/yuguolong/helen-data-processing/blob/master/png/232194_1.jpg)

# tip
考虑到python处理速度慢，加入了多进程处理，速度提升一倍以上（本人电脑性能差，好一点的电脑能提升2倍），加入了numba库装饰器，将numpy数据处理提升50倍以上。<br />
helen数据集共2300张图片，需处理23000张图片，本机耗时181秒


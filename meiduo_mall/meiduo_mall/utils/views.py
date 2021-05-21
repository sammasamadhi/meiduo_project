from django.contrib.auth.mixins import LoginRequiredMixin
from django import http

from meiduo_mall.utils.response_code import RETCODE


class LoginRequiredJSONMixin(LoginRequiredMixin):
    """自定义判断用户是否登陆的扩展类： 返回JSON"""

    # 为什么只需要重写handle_no_permission?
    # 因为判断用户是否登陆的操作，父类已经完成，子类只需要关心，如果用户未登陆，对应怎样的操作
    def handle_no_permission(self):
        return http.JsonResponse({'code': RETCODE.SESSIONERR, 'errmsg': '用户未登陆'})


"""
def handle_no_permission(self):
    if self.raise_exception:
        raise PermissionDenied(self.get_permission_denied_message())
    return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

class LoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
"""

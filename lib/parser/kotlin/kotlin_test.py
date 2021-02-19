import unittest

from model.component import Component
from lib.parser.kotlin import KotlinParser


class KotlinParserTest(unittest.TestCase):

    def test_should_parse_imports(self):
        src_code = """
        import com.nowocode.pesec.domain.auth.presenter.VerifyAuthPresenter
        import com.nowocode.pesec.domain.auth.presenter.VerifyAuthView
        import com.nowocode.pesec.domain.profile.ProfilePresenter
        import com.nowocode.pesec.domain.profile.ProfileView
        
        object AuthPresenterFactory {
            private val profilePresenter: ProfilePresenter =
                ProfilePresenter(
                    view = null,
                    authManager = ManagerFactory.authManager!!,
                    reportManager = ManagerFactory.reportManager!!
                )
            private val verifyAuthPresenter: VerifyAuthPresenter =
                VerifyAuthPresenter(view = null, authManager = ManagerFactory.authManager!!)
        
            fun getVerifyAuthPresenter(view: VerifyAuthView): VerifyAuthPresenter {
                this.verifyAuthPresenter.view = view
        
                return this.verifyAuthPresenter
            }
        
            fun getProfilePresenter(view: ProfileView): ProfilePresenter {
                this.profilePresenter.view = view
        
                return this.profilePresenter
    }
        """
        parser = KotlinParser()
        result = parser._parse_dependencies(src_code)
        expected_result = {
            "VerifyAuthPresenter":
                "com.nowocode.pesec.domain.auth.presenter",
            "VerifyAuthView":
                "com.nowocode.pesec.domain.auth.presenter",
            "ProfilePresenter":
                "com.nowocode.pesec.domain.profile",
            "ProfileView":
                "com.nowocode.pesec.domain.profile"
        }

        for k in result:
            self.assertTrue(expected_result[k.name] == k.package)

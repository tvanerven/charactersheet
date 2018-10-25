from django.views.generic import FormView
from charactersheet.forms.character_general_info import GeneralCharacterInfoForm


class CharacterGeneralInfoView(FormView):
    form_class = GeneralCharacterInfoForm
    success_url = '/charactersheet/new/'
    template_name = 'charactersheet/character_general_info.html'

    def form_valid(self, form):
        form.save()
        return super(CharacterGeneralInfoView, self).form_valid(form)

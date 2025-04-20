ive been thinking about how we will work with mode context and custom instructions and i think it is becoming apparent to me that we have created far to much custom instruction context for each mode and that we might want to shift from monolithic updates to the modes contexts to just ongoing improvements.

so for example,

what if we have a root .mode folder
and we dont nest the modes, we just name them as folders of the mode names, eg
.mode/accessibility-specialist
.mode/angular-developer
.mode/animejs-specialist
etc

and whatever we put in there can be potentially looked up by the mode when it is doing some work, it could check its readme in its custom-instructions folder eg
.modes/angular-developer/custom-instructions/README.md
except we change the custom-instructions to be 'kb'
so it would be
.modes/angular-developer/kb/README.md
which is more efficient and more meaningful for what is in there
and we can keep the context and examples folders, the user might put things there or we might in the future
so anyway the mode would decide when its checked the readme if any of the files in the /kb are going to be helpful for its assigned task and if it thinks so it would read the relevant ones into its context
and that could be a workspace level .roo/rules because that same rule would work fine for any mode, almost like before beginning work it checks its knowledgebase to see if it has something useful

i think we should revise the naming conventions for the modes eg

roo-commander
manager-projects
manager-products
lead-backend
lead-design
dev-angular
dev-tailwind
dev-react
dev-jquery
design-ui
design-mui
design-shadcn
etc

and i would like us to try harder to not use the same emoji for more than one mode, so start with roo commander, it gets the crown, and then we go to the manager level, pick the most appropriate emoji, and one by one we check the mode and decide on an emoji and if its taken we pick something else

that actually feels and reads kind of naturally to me, and i think with shorter names its less cluttered and dispenses with all the words like specialist and developer that take up so much character usage.

and i think we dont even need the footgun modes but we can have mode folders for the default modes like
.modes/code
.modes/debug
.modes/ask
.modes/architect
and the sub folders for each, context, kb, examples
in case we want to have some custom context for those modes

what do you think? what would you do differently? any problems with this ideas?
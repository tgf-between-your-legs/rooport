TITLE: Implementing Error Handling in Next.js Sign-in Form
DESCRIPTION: A React component for Next.js App Router that implements email/password sign-in with comprehensive error handling. Uses Clerk's useSignIn hook and displays validation errors to users.

LANGUAGE: typescript
CODE:
'use client'

import * as React from 'react'
import { useSignIn } from '@clerk/nextjs'
import { useRouter } from 'next/navigation'
import { ClerkAPIError } from '@clerk/types'
import { isClerkAPIResponseError } from '@clerk/nextjs/errors'

export default function SignInForm() {
  const { isLoaded, signIn, setActive } = useSignIn()
  const [email, setEmail] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [errors, setErrors] = React.useState<ClerkAPIError[]>()

  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setErrors(undefined)
    if (!isLoaded) return
    try {
      const signInAttempt = await signIn.create({
        identifier: email,
        password,
      })
      if (signInAttempt.status === 'complete') {
        await setActive({ session: signInAttempt.createdSessionId })
        router.push('/')
      } else {
        console.error(JSON.stringify(signInAttempt, null, 2))
      }
    } catch (err) {
      if (isClerkAPIResponseError(err)) setErrors(err.errors)
      console.error(JSON.stringify(err, null, 2))
    }
  }

  return (
    <>
      <h1>Sign in</h1>
      <form onSubmit={(e) => handleSubmit(e)}>
        <div>
          <label htmlFor="email">Enter email address</label>
          <input
            onChange={(e) => setEmail(e.target.value)}
            id="email"
            name="email"
            type="email"
            value={email}
          />
        </div>
        <div>
          <label htmlFor="password">Enter password</label>
          <input
            onChange={(e) => setPassword(e.target.value)}
            id="password"
            name="password"
            type="password"
            value={password}
          />
        </div>
        <button type="submit">Sign in</button>
      </form>

      {errors && (
        <ul>
          {errors.map((el, index) => (
            <li key={index}>{el.longMessage}</li>
          ))}
        </ul>
      )}
    </>
  )

----------------------------------------

TITLE: Accessing User Data in Next.js Pages Router getServerSideProps
DESCRIPTION: This example shows how to use getAuth(), clerkClient(), and buildClerkProps() helpers in a Next.js Pages Router getServerSideProps function to protect routes and access user data.

LANGUAGE: tsx
CODE:
import { getAuth, buildClerkProps } from '@clerk/nextjs/server'
import { GetServerSideProps } from 'next'

export const getServerSideProps: GetServerSideProps = async (ctx) => {
  // Use `getAuth()` to get the user's ID
  const { userId } = getAuth(ctx.req)

  // Protect the route by checking if the user is signed in
  if (!userId) {
    // Handle when the user is not signed in
  }

  // Initialize the Backend SDK
  const client = await clerkClient()

  // Get the user's full `Backend User` object
  const user = userId ? await client.users.getUser(userId) : undefined

  return { props: { ...buildClerkProps(ctx.req, { user }) } }
}

----------------------------------------

TITLE: Preparing Email Verification with SignUp Class
DESCRIPTION: Method to initiate email verification process by sending a verification code or link to the user's email address. Supports both email_code and email_link strategies with optional parameters.

LANGUAGE: typescript
CODE:
function prepareEmailAddressVerification(
  params?: PrepareEmailAddressVerificationParams,
): Promise<SignUpResource>

----------------------------------------

TITLE: Creating Protected tRPC Procedure with Authentication Middleware
DESCRIPTION: Demonstrates how to create a protected tRPC procedure using middleware that checks for user authentication.

LANGUAGE: typescript
CODE:
const isAuthed = t.middleware(({ next, ctx }) => {
  if (!ctx.auth.userId) {
    throw new TRPCError({ code: 'UNAUTHORIZED' })
  }
  return next({
    ctx: {
      auth: ctx.auth,
    },
  })
})

export const router = t.router
export const publicProcedure = t.procedure
export const protectedProcedure = t.procedure.use(isAuthed)

----------------------------------------

TITLE: Verifying Session with Clerk Backend SDK in TypeScript
DESCRIPTION: This snippet demonstrates how to use the deprecated `verifySession()` method from Clerk's Backend SDK to verify a session. It requires a session ID and token as input parameters.

LANGUAGE: tsx
CODE:
const sessionId = 'my-session-id'

const token = 'my-session-token'

const session = await clerkClient.sessions.verifySession(sessionId, token)

----------------------------------------

TITLE: Expo React Native Authentication Flow
DESCRIPTION: React Native implementation of authentication flow for Expo applications using Clerk. Includes both sign-up and sign-in functionality.

LANGUAGE: typescript
CODE:
import * as React from 'react'
import { Text, TextInput, Button, View } from 'react-native'
// Expo implementation...

----------------------------------------

TITLE: Implementing Clerk Middleware
DESCRIPTION: Setting up Clerk middleware to handle authentication state and route protection in Next.js application.

LANGUAGE: tsx
CODE:
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    '/((?!_next|[^?]*\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    '/(api|trpc)(.*)',
  ],
}

----------------------------------------

TITLE: Integrating ClerkProvider in Next.js App Router
DESCRIPTION: This snippet demonstrates how to wrap a Next.js application with ClerkProvider using the App Router. It provides session and user context to the entire application.

LANGUAGE: tsx
CODE:
import React from 'react'
import { ClerkProvider } from '@clerk/nextjs'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}

----------------------------------------

TITLE: Implementing Sign-in Flow with Clerk Elements and shadcn/ui
DESCRIPTION: React component for a custom sign-in flow using Clerk Elements and shadcn/ui components. Includes social login options, email/password fields, and multiple authentication strategies.

LANGUAGE: tsx
CODE:
'use client'
import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'
import Link from 'next/link'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Icons } from '@/components/ui/icons'
import { cn } from '@/lib/utils'

export default function SignInPage() {
  return (
    <div className="grid w-full grow items-center px-4 sm:justify-center">
      <SignIn.Root>
        <Clerk.Loading>
          {(isGlobalLoading) => (
            <>
              <SignIn.Step name="start">
                <Card className="w-full sm:w-96">
                  <CardHeader>
                    <CardTitle>Sign in to Acme Co</CardTitle>
                    <CardDescription>Welcome back! Please sign in to continue</CardDescription>
                  </CardHeader>
                  <CardContent className="grid gap-y-4">
                    <div className="grid grid-cols-2 gap-x-4">
                      <Clerk.Connection name="github" asChild>
                        <Button
                          size="sm"
                          variant="outline"
                          type="button"
                          disabled={isGlobalLoading}
                        >
                          <Clerk.Loading scope="provider:github">
                            {(isLoading) =>
                              isLoading ? (
                                <Icons.spinner className="size-4 animate-spin" />
                              ) : (
                                <>
                                  <Icons.gitHub className="mr-2 size-4" />
                                  GitHub
                                </>
                              )
                            }
                          </Clerk.Loading>
                        </Button>
                      </Clerk.Connection>
                      <Clerk.Connection name="google" asChild>
                        <Button
                          size="sm"
                          variant="outline"
                          type="button"
                          disabled={isGlobalLoading}
                        >
                          <Clerk.Loading scope="provider:google">
                            {(isLoading) =>
                              isLoading ? (
                                <Icons.spinner className="size-4 animate-spin" />
                              ) : (
                                <>
                                  <Icons.google className="mr-2 size-4" />
                                  Google
                                </>
                              )
                            }
                          </Clerk.Loading>
                        </Button>
                      </Clerk.Connection>
                    </div>
                    <p className="flex items-center gap-x-3 text-sm text-muted-foreground before:h-px before:flex-1 before:bg-border after:h-px after:flex-1 after:bg-border">
                      or
                    </p>
                    <Clerk.Field name="identifier" className="space-y-2">
                      <Clerk.Label asChild>
                        <Label>Email address</Label>
                      </Clerk.Label>
                      <Clerk.Input type="email" required asChild>
                        <Input />
                      </Clerk.Input>
                      <Clerk.FieldError className="block text-sm text-destructive" />
                    </Clerk.Field>
                  </CardContent>
                  <CardFooter>
                    <div className="grid w-full gap-y-4">
                      <SignIn.Action submit asChild>
                        <Button disabled={isGlobalLoading}>
                          <Clerk.Loading>
                            {(isLoading) => {
                              return isLoading ? (
                                <Icons.spinner className="size-4 animate-spin" />
                              ) : (
                                'Continue'
                              )
                            }}
                          </Clerk.Loading>
                        </Button>
                      </SignIn.Action>

                      <Button variant="link" size="sm" asChild>
                        <Clerk.Link navigate="sign-up">
                          Don&apos;t have an account? Sign up
                        </Clerk.Link>
                      </Button>
                    </div>
                  </CardFooter>
                </Card>
              </SignIn.Step>

              <SignIn.Step name="choose-strategy">
                <Card className="w-full sm:w-96">
                  <CardHeader>
                    <CardTitle>Use another method</CardTitle>
                    <CardDescription>
                      Facing issues? You can use any of these methods to sign in.
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="grid gap-y-4">
                    <SignIn.SupportedStrategy name="email_code" asChild>
                      <Button type="button" variant="link" disabled={isGlobalLoading}>
                        Email code
                      </Button>
                    </SignIn.SupportedStrategy>
                    <SignIn.SupportedStrategy name="password" asChild>
                      <Button type="button" variant="link" disabled={isGlobalLoading}>
                        Password
                      </Button>
                    </SignIn.SupportedStrategy>
                  </CardContent>
                  <CardFooter>
                    <div className="grid w-full gap-y-4">
                      <SignIn.Action navigate="previous" asChild>
                        <Button disabled={isGlobalLoading}>
                          <Clerk.Loading>
                            {(isLoading) => {
                              return isLoading ? (
                                <Icons.spinner className="size-4 animate-spin" />
                              ) : (
                                'Go back'
                              )
                            }}
                          </Clerk.Loading>
                        </Button>
                      </SignIn.Action>
                    </div>
                  </CardFooter>
                </Card>
              </SignIn.Step>

              <SignIn.Step name="verifications">
                <SignIn.Strategy name="password">
                  <Card className="w-full sm:w-96">
                    <CardHeader>
                      <CardTitle>Check your email</CardTitle>
                      <CardDescription>
                        Enter the verification code sent to your email
                      </CardDescription>
                      <p className="text-sm text-muted-foreground">
                        Welcome back <SignIn.SafeIdentifier />
                      </p>
                    </CardHeader>
                    <CardContent className="grid gap-y-4">
                      <Clerk.Field name="password" className="space-y-2">
                        <Clerk.Label asChild>
                          <Label>Password</Label>
                        </Clerk.Label>
                        <Clerk.Input type="password" asChild>
                          <Input />
                        </Clerk.Input>
                        <Clerk.FieldError className="block text-sm text-destructive" />
                      </Clerk.Field>
                    </CardContent>
                    <CardFooter>
                      <div className="grid w-full gap-y-4">
                        <SignIn.Action submit asChild>
                          <Button disabled={isGlobalLoading}>
                            <Clerk.Loading>
                              {(isLoading) => {
                                return isLoading ? (
                                  <Icons.spinner className="size-4 animate-spin" />
                                ) : (
                                  'Continue'
                                )
                              }}
                            </Clerk.Loading>
                          </Button>
                        </SignIn.Action>
                        <SignIn.Action navigate="choose-strategy" asChild>
                          <Button type="button" size="sm" variant="link">
                            Use another method
                          </Button>
                        </SignIn.Action>
                      </div>
                    </CardFooter>
                  </Card>
                </SignIn.Strategy>

                <SignIn.Strategy name="email_code">
                  <Card className="w-full sm:w-96">
                    <CardHeader>
                      <CardTitle>Check your email</CardTitle>
                      <CardDescription>
                        Enter the verification code sent to your email
                      </CardDescription>
                      <p className="text-sm text-muted-foreground">
                        Welcome back <SignIn.SafeIdentifier />
                      </p>
                    </CardHeader>
                    <CardContent className="grid gap-y-4">
                      <Clerk.Field name="code">
                        <Clerk.Label className="sr-only">Email verification code</Clerk.Label>
                        <div className="grid gap-y-2 items-center justify-center">
                          <div className="flex justify-center text-center">
                            <Clerk.Input
                              type="otp"
                              autoSubmit
                              className="flex justify-center has-[:disabled]:opacity-50"
                              render={({ value, status }) => {
                                return (
                                  <div
                                    data-status={status}
                                    className="relative flex h-9 w-9 items-center justify-center border-y border-r border-input text-sm shadow-sm transition-all first:rounded-l-md first:border-l last:rounded-r-md data-[status=selected]:ring-1 data-[status=selected]:ring-ring data-[status=cursor]:ring-1 data-[status=cursor]:ring-ring"
                                  >
                                    {value}
                                  </div>
                                )
                              }}
                            />
                          </div>
                          <Clerk.FieldError className="block text-sm text-destructive text-center" />
                          <SignIn.Action
                            asChild
                            resend
                            className="text-muted-foreground"
                            fallback={({ resendableAfter }) => (
                              <Button variant="link" size="sm" disabled>
                                Didn&apos;t receive a code? Resend (
                                <span className="tabular-nums">{resendableAfter}</span>)
                              </Button>
                            )}
                          >
                            <Button variant="link" size="sm">
                              Didn&apos;t receive a code? Resend
                            </Button>
                          </SignIn.Action>
                        </div>
                      </Clerk.Field>
                    </CardContent>
                    <CardFooter>
                      <div className="grid w-full gap-y-4">
                        <SignIn.Action submit asChild>
                          <Button disabled={isGlobalLoading}>
                            <Clerk.Loading>
                              {(isLoading) => {
                                return isLoading ? (
                                  <Icons.spinner className="size-4 animate-spin" />
                                ) : (
                                  'Continue'
                                )
                              }}
                            </Clerk.Loading>
                          </Button>
                        </SignIn.Action>
                        <SignIn.Action navigate="choose-strategy" asChild>
                          <Button size="sm" variant="link">
                            Use another method
                          </Button>
                        </SignIn.Action>
                      </div>
                    </CardFooter>
                  </Card>
                </SignIn.Strategy>
              </SignIn.Step>
            </>
          )}
        </Clerk.Loading>
      </SignIn.Root>
    </div>
  )
}

----------------------------------------

TITLE: Implementing Clerk Middleware in Next.js
DESCRIPTION: Setting up Clerk middleware to handle authentication state throughout the app. This code exports the clerkMiddleware and configures the matcher for specific routes.

LANGUAGE: tsx
CODE:
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}

----------------------------------------

TITLE: Implementing Username/Password Sign-in with Clerk Elements
DESCRIPTION: A complete implementation of a username/password sign-in flow using Clerk Elements. Features styled form inputs for username and password with error handling and navigation to sign-up.

LANGUAGE: tsx
CODE:
'use client'

import * as Clerk from '@clerk/elements/common'
import * as SignIn from '@clerk/elements/sign-in'

export default function SignInPage() {
  return (
    <div className="grid w-full flex-grow items-center bg-zinc-100 px-4 sm:justify-center">
      <SignIn.Root>
        <SignIn.Step
          name="start"
          className="w-full space-y-6 rounded-2xl bg-white px-4 py-10 shadow-md ring-1 ring-black/5 sm:w-96 sm:px-8"
        >
          <!-- Component implementation details -->
        </SignIn.Step>
      </SignIn.Root>
    </div>
  )
}

----------------------------------------

TITLE: Protecting Server Actions with Clerk Auth in Next.js
DESCRIPTION: This snippet shows how to use the auth() helper from Clerk to protect a server action in a Server Component. It checks if the user is signed in before allowing the action to proceed.

LANGUAGE: tsx
CODE:
import { auth } from '@clerk/nextjs/server'

export default function AddToCart() {
  async function addItem(formData: FormData) {
    'use server'

    const { userId } = await auth()

    if (!userId) {
      throw new Error('You must be signed in to add an item to your cart')
    }

    console.log('add item server action', formData)
  }

  return (
    <form action={addItem}>
      <input value={'test'} type="text" name="name" />
      <button type="submit">Add to Cart</button>
    </form>
  )
}

----------------------------------------

TITLE: Using auth() Helper in Next.js Server Components
DESCRIPTION: Demonstrates how to use Clerk's auth() helper function in a Next.js server component to access authentication data dynamically at request time. This approach opts the entire route into dynamic rendering.

LANGUAGE: tsx
CODE:
import { auth } from '@clerk/nextjs/server'

// This page will be dynamically rendered at request time
export default async function Page() {
  const { userId } = await auth()

  return <p>Hello, {userId}</p>
}

----------------------------------------

TITLE: Basic Clerk Middleware Configuration in Next.js
DESCRIPTION: Basic setup of clerkMiddleware() in a Next.js application with route matcher configuration to skip static files and include API routes.

LANGUAGE: typescript
CODE:
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    '/((?!_next|[^?]*\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    '/(api|trpc)(.*)',
  ],
}

----------------------------------------

TITLE: State-Based Styling with Data Attributes in CSS
DESCRIPTION: Demonstrates how to use data attributes for state-based styling of Clerk Elements components. This approach allows for styling based on the validity state of form fields.

LANGUAGE: css
CODE:
.input {
  --border-color: gray;
  border: 1px solid var(--border-color);

  &[data-invalid] {
    --border-color: red;
  }
}

----------------------------------------

TITLE: Using Clerk Backend SDK Standalone in TypeScript
DESCRIPTION: Example of using the Clerk Backend SDK on its own to authenticate a request. It demonstrates creating a Clerk client with environment variables and using it to authenticate an incoming request.

LANGUAGE: tsx
CODE:
import { createClerkClient } from '@clerk/backend'

export async function GET(req: Request) {
  const clerkClient = createClerkClient({
    secretKey: process.env.CLERK_SECRET_KEY,
    publishableKey: process.env.CLERK_PUBLISHABLE_KEY,
  })

  const { isSignedIn } = await clerkClient.authenticateRequest(req, {
    authorizedParties: ['https://example.com'],
  })

  if (!isSignedIn) {
    return Response.json({ status: 401 })
  }

  // Add logic to perform protected actions

  return Response.json({ message: 'This is a reply' })
}

----------------------------------------

TITLE: Importing Auth Object in Next.js App Router
DESCRIPTION: Demonstrates how to import and use the auth() function in the Next.js App Router. This function returns an Auth object containing important user session information.

LANGUAGE: javascript
CODE:
import { auth } from "@clerk/nextjs";

----------------------------------------

TITLE: React Custom Hook for Authenticated Fetch
DESCRIPTION: Custom hook implementation for making authenticated requests in React applications. Uses the useAuth hook to get the session token and includes it in the Authorization header.

LANGUAGE: jsx
CODE:
export default async function useFetch() {
  const { getToken } = useAuth()

  const token = await getToken()

  const authenticatedFetch = async (...args) => {
    return fetch(...args, {
      headers: { Authorization: `Bearer ${token}` },
    }).then((res) => res.json())
  }
  return authenticatedFetch
}
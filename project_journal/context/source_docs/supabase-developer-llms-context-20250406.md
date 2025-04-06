TITLE: Enabling pgvector Extension in Postgres
DESCRIPTION: SQL command to enable the pgvector extension for vector operations in Postgres.

LANGUAGE: sql
CODE:
create extension vector
with
  schema extensions;

----------------------------------------

TITLE: Creating Function with Custom Timeout in PostgreSQL
DESCRIPTION: Defines a function 'myfunc' with a custom statement timeout of 4 seconds. This approach allows setting timeouts for specific functions, useful for recurring functions that need special runtime exemptions.

LANGUAGE: sql
CODE:
create or replace function myfunc()
returns void as $$
 select pg_sleep(3); -- simulating some long-running process
$$
language sql
set statement_timeout TO '4s'; -- set custom timeout

----------------------------------------

TITLE: Adding Supabase Status Feed to Slack
DESCRIPTION: Slack command for subscribing to Supabase platform status updates using the built-in RSS functionality

LANGUAGE: shell
CODE:
/feed subscribe https://status.supabase.com/history.atom

----------------------------------------

TITLE: Basic Full Text Search Query in PostgreSQL
DESCRIPTION: SQL and various language examples to perform a basic full text search on a single column.

LANGUAGE: sql
CODE:
select
  *
from
  books
where
  to_tsvector(description)
  @@ to_tsquery('big');

LANGUAGE: javascript
CODE:
const { data, error } = await supabase.from('books').select().textSearch('description', `'big'`)

LANGUAGE: dart
CODE:
final result = await client
  .from('books')
  .select()
  .textSearch('description', "'big'");

LANGUAGE: swift
CODE:
let response = await client.from("books")
  .select()
  .textSearch("description", value: "'big'")
  .execute()

LANGUAGE: kotlin
CODE:
val data = supabase.from("books").select {
    filter {
        textSearch("description", "'big'", TextSearchType.NONE)
    }
}

LANGUAGE: python
CODE:
data = supabase.from_('books').select().text_search('description', "'big'").execute()

----------------------------------------

TITLE: Creating Document Storage Schema in SQL
DESCRIPTION: SQL schema creation for storing documents and their sections with vector embeddings, including owner tracking through foreign key relationships.

LANGUAGE: sql
CODE:
create table documents (
  id bigint primary key generated always as identity,
  name text not null,
  owner_id uuid not null references auth.users (id) default auth.uid(),
  created_at timestamp with time zone not null default now()
);

create table document_sections (
  id bigint primary key generated always as identity,
  document_id bigint not null references documents (id),
  content text not null,
  embedding vector (384)
);

----------------------------------------

TITLE: React/JSX Component Mapping Example
DESCRIPTION: A React/JSX code snippet that maps through framework quickstart options to render GlassPanel components wrapped in Link elements.

LANGUAGE: jsx
CODE:
{[
    {
      title: 'Next.js',
      href: '/guides/auth/server-side/nextjs',
      description:
        'Automatically configure Supabase in Next.js to use cookies, making your user and their session available on the client and server.',
      icon: '/docs/img/icons/nextjs-icon',
    },
    {
      title: 'SvelteKit',
      href: '/guides/auth/server-side/sveltekit',
      description:
        'Automatically configure Supabase in SvelteKit to use cookies, making your user and their session available on the client and server.',
      icon: '/docs/img/icons/svelte-icon',
    },
  ].map((item) => {
    return (
      <Link href={`${item.href}`} key={item.title} passHref>
        <GlassPanel title={item.title} background={false} icon={item.icon}>
          {item.description}
        </GlassPanel>
      </Link>
    )
  })}

----------------------------------------

TITLE: Enforcing MFA for New Users in PostgreSQL
DESCRIPTION: This SQL snippet creates a restrictive Row Level Security policy that enforces MFA for new users created after a specific date, while allowing both 'aal1' and 'aal2' levels for existing users.

LANGUAGE: sql
CODE:
create policy "Policy name."
  on table_name
  as restrictive -- very important!
  to authenticated
  using
    (array[(select auth.jwt()->>'aal')] <@ (
       select
         case
           when created_at >= '2022-12-12T00:00:00Z' then array['aal2']
           else array['aal1', 'aal2']
         end as aal
       from auth.users
       where (select auth.uid()) = id));

----------------------------------------

TITLE: Creating a Policy Using auth.jwt() Function
DESCRIPTION: This SQL snippet demonstrates how to use the auth.jwt() function in a policy to check if a user belongs to a team.

LANGUAGE: sql
CODE:
create policy "User is in team"
on my_table
to authenticated
using ( team_id in (select auth.jwt() -> 'app_metadata' -> 'teams'));

----------------------------------------

TITLE: Implementing Spotify OAuth Sign In - JavaScript
DESCRIPTION: JavaScript implementation for signing in users with Spotify OAuth using Supabase Auth. Uses the signInWithOAuth method with 'spotify' as the provider.

LANGUAGE: javascript
CODE:
async function signInWithSpotify() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'spotify',
  })
}

----------------------------------------

TITLE: Creating an UPDATE Policy for User Profiles
DESCRIPTION: This SQL snippet shows how to create a policy that allows users to update only their own profile.

LANGUAGE: sql
CODE:
create table profiles (
  id uuid primary key,
  user_id uuid references auth.users,
  avatar_url text
);

alter table profiles enable row level security;

create policy "Users can update their own profile."
on profiles for update
to authenticated
using ( (select auth.uid()) = user_id )
with check ( (select auth.uid()) = user_id );

----------------------------------------

TITLE: Initializing Supabase Project
DESCRIPTION: Initialize a new Supabase project using the CLI command.

LANGUAGE: shell
CODE:
supabase init

----------------------------------------

TITLE: Role Permissions Seed Data
DESCRIPTION: SQL code for inserting initial role permissions data into the database.

LANGUAGE: sql
CODE:
insert into public.role_permissions (role, permission)
values
  ('admin', 'channels.delete'),
  ('admin', 'messages.delete'),
  ('moderator', 'messages.delete');

----------------------------------------

TITLE: Setting up environment variables for Supabase in Next.js
DESCRIPTION: Create a .env.local file with Supabase URL and anonymous key for Next.js application.

LANGUAGE: text
CODE:
NEXT_PUBLIC_SUPABASE_URL=<your_supabase_project_url>
NEXT_PUBLIC_SUPABASE_ANON_KEY=<your_supabase_anon_key>

----------------------------------------

TITLE: Creating Vector Table in PostgreSQL
DESCRIPTION: SQL command to create a table that can store vector embeddings. The table includes columns for ID, title, body text, and a vector embedding of dimension 384.

LANGUAGE: sql
CODE:
create table posts (
  id serial primary key,
  title text not null,
  body text not null,
  embedding vector(384)
);

----------------------------------------

TITLE: Implementing Login and Signup Actions
DESCRIPTION: Server-side actions for handling user login and signup using Supabase authentication.

LANGUAGE: javascript
CODE:
'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'
import { createClient } from '@/utils/supabase/server'

export async function login(formData) {
  const supabase = await createClient()
  const data = {
    email: formData.get('email'),
    password: formData.get('password'),
  }
  const { error } = await supabase.auth.signInWithPassword(data)
  if (error) {
    redirect('/error')
  }
  revalidatePath('/', 'layout')
  redirect('/account')
}

export async function signup(formData) {
  const supabase = await createClient()
  const data = {
    email: formData.get('email'),
    password: formData.get('password'),
  }
  const { error } = await supabase.auth.signUp(data)
  if (error) {
    redirect('/error')
  }
  revalidatePath('/', 'layout')
  redirect('/account')
}

----------------------------------------

TITLE: Creating IVFFlat Index for Inner Product in SQL
DESCRIPTION: SQL command to create an IVFFlat index using the vector_ip_ops operator class for inner product distance. The index is created on the 'column_name' of the 'items' table with 100 lists.

LANGUAGE: sql
CODE:
create index on items using ivfflat (column_name vector_ip_ops) with (lists = 100);

----------------------------------------

TITLE: Creating an Index for RLS Performance
DESCRIPTION: This SQL snippet demonstrates how to create an index to improve RLS performance on a frequently used column in policies.

LANGUAGE: sql
CODE:
create index userid
on test_table
using btree (user_id);

----------------------------------------

TITLE: Creating trigger function for new user profiles in SQL for Supabase
DESCRIPTION: SQL code to create a function and trigger that automatically inserts a row into public.profiles when a new user is created in auth.users.

LANGUAGE: sql
CODE:
-- inserts a row into public.profiles
create function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = ''
as $$
begin
  insert into public.profiles (id, first_name, last_name)
  values (new.id, new.raw_user_meta_data ->> 'first_name', new.raw_user_meta_data ->> 'last_name');
  return new;
end;
$$;

-- trigger the function every time a user is created
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

----------------------------------------

TITLE: Creating a DELETE Policy for User Profiles
DESCRIPTION: This SQL snippet demonstrates how to create a policy that allows users to delete only their own profile.

LANGUAGE: sql
CODE:
create table profiles (
  id uuid primary key,
  user_id uuid references auth.users,
  avatar_url text
);

alter table profiles enable row level security;

create policy "Users can delete a profile."
on profiles for delete
to authenticated
using ( (select auth.uid()) = user_id );

----------------------------------------

TITLE: Advanced Full Text Search Query with Proximity Operator
DESCRIPTION: SQL and various language examples to perform a full text search using the proximity operator.

LANGUAGE: sql
CODE:
select
  *
from
  books
where
  to_tsvector(description) @@ to_tsquery('big <-> dreams');

LANGUAGE: javascript
CODE:
const { data, error } = await supabase
  .from('books')
  .select()
  .textSearch('description', `'big' <-> 'dreams'`)

LANGUAGE: dart
CODE:
final result = await client
  .from('books')
  .select()
  .textSearch('description', "'big' <-> 'dreams'");

LANGUAGE: swift
CODE:
let response = try await client
  .from("books")
  .select()
  .textSearch("description", value: "'big' <-> 'dreams'")
  .execute()

LANGUAGE: kotlin
CODE:
val data = supabase.from("books").select {
    filter {
        textSearch("description", "'big' <-> 'dreams'", TextSearchType.NONE)
    }
}

LANGUAGE: python
CODE:
data = client.from_('books').select().text_search('description', "'big' <-> 'dreams'").execute()

----------------------------------------

TITLE: Implementing Supabase Auth in React
DESCRIPTION: React component implementation that initializes Supabase client and handles authentication state using the Auth UI component. Includes session management and auth state change subscription.

LANGUAGE: javascript
CODE:
import './index.css'
import { useState, useEffect } from 'react'
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient('https://<project>.supabase.co', '<your-anon-key>')

export default function App() {
  const [session, setSession] = useState(null)

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session)
    })

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setSession(session)
    })

    return () => subscription.unsubscribe()
  }, [])

  if (!session) {
    return (<Auth supabaseClient={supabase} appearance={{ theme: ThemeSupa }} />)
  }
  else {
    return (<div>Logged in!</div>)
  }
}

----------------------------------------

TITLE: Querying Todos with Client Libraries
DESCRIPTION: Examples of fetching todos using various Supabase client libraries.

LANGUAGE: javascript
CODE:
const { data, error } = await supabase.from('todos').select()

LANGUAGE: dart
CODE:
final data = await supabase.from('todos').select('*');

LANGUAGE: python
CODE:
response = supabase.table('todos').select("*").execute()

LANGUAGE: swift
CODE:
let response = try await supabase.from("todos").select()

----------------------------------------

TITLE: Creating React Application
DESCRIPTION: Command to create a new React application using create-react-app scaffolding tool.

LANGUAGE: bash
CODE:
npx create-react-app my-app

----------------------------------------

TITLE: Creating a Hybrid Structured and Unstructured Metadata Table in SQL
DESCRIPTION: This SQL snippet creates a table that combines structured metadata columns with an unstructured JSONB column. It allows for both known fields with dedicated columns and flexible unknown fields in the JSON data.

LANGUAGE: sql
CODE:
create table docs (
  id uuid primary key,
  embedding vector(3),
  content text,
  url string,
  meta jsonb
);

insert into docs
  (id, embedding, content, url, meta)
values
  (
    '79409372-7556-4ccc-ab8f-5786a6cfa4f7',
    array[0.1, 0.2, 0.3],
    'Hello world',
    '/hello-world',
    '{"key": "value"}'
  );

----------------------------------------

TITLE: Using Generated Types with supabase-js v2
DESCRIPTION: This example demonstrates how to use the generated TypeScript types to enhance type support when interacting with the Supabase client in v2.

LANGUAGE: typescript
CODE:
import type { Database } from './DatabaseDefinitions'

const supabase = createClient<Database>(SUPABASE_URL, ANON_KEY)

const { data } = await supabase.from('messages').select().match({ id: 1 })

----------------------------------------

TITLE: Executing a Database Function in SQL and Various Client Libraries
DESCRIPTION: This snippet shows how to execute the 'hello_world' function using SQL and different Supabase client libraries.

LANGUAGE: sql
CODE:
select hello_world();

LANGUAGE: javascript
CODE:
const { data, error } = await supabase.rpc('hello_world')

LANGUAGE: dart
CODE:
final data = await supabase
  .rpc('hello_world');

LANGUAGE: swift
CODE:
try await supabase.rpc("hello_world").execute()

LANGUAGE: kotlin
CODE:
val data = supabase.postgrest.rpc("hello_world")

LANGUAGE: python
CODE:
data = supabase.rpc('hello_world').execute()

----------------------------------------

TITLE: Inserting Data into a Table using JavaScript
DESCRIPTION: JavaScript code using Supabase client to insert multiple rows into the 'movies' table.

LANGUAGE: javascript
CODE:
const { data, error } = await supabase.from('movies').insert([
  {
    name: 'The Empire Strikes Back',
    description:
      'After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda.',
  },
  {
    name: 'Return of the Jedi',
    description:
      'After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star.',
  },
])

----------------------------------------

TITLE: Connecting to Supabase Database with Drizzle ORM
DESCRIPTION: Set up a connection to the Supabase database using the Connection Pooler and Drizzle ORM. This code uses environment variables for the database URL.

LANGUAGE: typescript
CODE:
import 'dotenv/config'

import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'

const connectionString = process.env.DATABASE_URL

// Disable prefetch as it is not supported for "Transaction" pool mode
export const client = postgres(connectionString, { prepare: false })
export const db = drizzle(client);

----------------------------------------

TITLE: Signing in with Magic Link using Supabase Auth in JavaScript
DESCRIPTION: This code snippet demonstrates how to implement Magic Link authentication using Supabase Auth in JavaScript. It includes options for preventing automatic user creation and specifying a redirect URL.

LANGUAGE: javascript
CODE:
async function signInWithEmail() {
  const { data, error } = await supabase.auth.signInWithOtp({
    email: 'valid.email@supabase.io',
    options: {
      // set this to false if you do not want the user to be automatically signed up
      shouldCreateUser: false,
      emailRedirectTo: 'https://example.com/welcome',
    },
  })
}

----------------------------------------

TITLE: Initializing Supabase Vecs Client in Python
DESCRIPTION: Sets up a connection to Supabase database using vecs client. Requires a valid PostgreSQL connection string with pooling support for Google Colab compatibility.

LANGUAGE: python
CODE:
import vecs

DB_CONNECTION = "postgresql://<user>:<password>@<host>:<port>/<db_name>"

# create vector store client
vx = vecs.create_client(DB_CONNECTION)

----------------------------------------

TITLE: Enforcing MFA for All Users in PostgreSQL
DESCRIPTION: This SQL snippet creates a restrictive Row Level Security policy that enforces MFA for all authenticated users by requiring an 'aal2' level JWT.

LANGUAGE: sql
CODE:
create policy "Policy name."
  on table_name
  as restrictive
  to authenticated
  using ((select auth.jwt()->>'aal') = 'aal2');

----------------------------------------

TITLE: Configuring Next.js Middleware for Supabase Auth
DESCRIPTION: Set up middleware to handle session refreshing and route protection for Supabase authentication.

LANGUAGE: javascript
CODE:
import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs'
import { NextResponse } from 'next/server'

export async function middleware(req) {
  const res = NextResponse.next()
  const supabase = createMiddlewareClient({ req, res })
  await supabase.auth.getUser()
  return res
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
}

----------------------------------------

TITLE: Implementing Next.js Middleware for Session Management
DESCRIPTION: Setup of Next.js middleware to handle Supabase authentication and session management

LANGUAGE: typescript
CODE:
import { createServerClient } from '@supabase/ssr'
import { NextResponse, type NextRequest } from 'next/server'

export async function updateSession(request: NextRequest) {
  let supabaseResponse = NextResponse.next({
    request,
  })

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll()
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) => request.cookies.set(name, value))
          supabaseResponse = NextResponse.next({
            request,
          })
          cookiesToSet.forEach(({ name, value, options }) =>
            supabaseResponse.cookies.set(name, value, options)
          )
        },
      },
    }
  )

  const {
    data: { user },
  } = await supabase.auth.getUser()

  return supabaseResponse
}

----------------------------------------

TITLE: Configuring Column Level Privileges in PostgreSQL
DESCRIPTION: Revokes table-level UPDATE privilege and grants column-level UPDATE privilege on specific columns for the authenticated role.

LANGUAGE: sql
CODE:
revoke
update
  on table public.posts
from
  authenticated;

grant
update
  (title, content) on table public.posts to authenticated;

----------------------------------------

TITLE: Using TypeScript with Supabase.js v2
DESCRIPTION: Demonstrates how to use TypeScript with Supabase.js v2, including importing database definitions and creating a typed client.

LANGUAGE: ts
CODE:
import type { Database } from './DatabaseDefinitions'

const supabase = createClient<Database>(SUPABASE_URL, ANON_KEY)

const { data } = await supabase.from('messages').select().match({ id: 1 })

----------------------------------------

TITLE: Creating an INSERT Policy for Authenticated Users
DESCRIPTION: This SQL snippet demonstrates how to create a policy that allows authenticated users to insert their own profile.

LANGUAGE: sql
CODE:
create table profiles (
  id uuid primary key,
  user_id uuid references auth.users,
  avatar_url text
);

alter table profiles enable row level security;

create policy "Users can create a profile."
on profiles for insert
to authenticated
with check ( (select auth.uid()) = user_id );

----------------------------------------

TITLE: Enabling pg_stat_statements Extension in PostgreSQL
DESCRIPTION: SQL commands to enable and disable the pg_stat_statements extension. It's recommended to create the extension within a separate schema to keep the public schema clean.

LANGUAGE: sql
CODE:
-- Enable the "pg_stat_statements" extension
create extension pg_stat_statements with schema extensions;

-- Disable the "pg_stat_statements" extension
drop extension if exists pg_stat_statements;

----------------------------------------

TITLE: Protecting API Routes in SvelteKit
DESCRIPTION: TypeScript code for protecting an API route in SvelteKit using Supabase authentication.

LANGUAGE: typescript
CODE:
import { json, error } from '@sveltejs/kit'

export const GET = async ({ locals: { supabase, safeGetSession } }) => {
  const { session } = await safeGetSession()
  if (!session) {
    // the user is not signed in
    throw error(401, { message: 'Unauthorized' })
  }
  const { data } = await supabase.from('test').select('*')

  return json({ data })
}

----------------------------------------

TITLE: Connecting to a Realtime Channel in TypeScript
DESCRIPTION: This snippet demonstrates how to connect to a Supabase Realtime Channel using the Supabase JavaScript client. It shows the process of creating a client, setting authentication, and subscribing to a channel.

LANGUAGE: tsx
CODE:
import { createClient } from '@supabase/supabase-js'

// Prepare client with authenticated user
const client = createClient('<url>', '<anon_key>')
client.realtime.setAuth(token)

// Prepare the realtime channel
const channel = client.channel('topic')

channel
.subscribe((status: string, err: any) => {
  if (status === 'SUBSCRIBED') {
    console.log('Connected')
  }
})

----------------------------------------

TITLE: Creating a Table with Primary Key in SQL
DESCRIPTION: SQL command to create a table named 'movies' with an auto-incrementing primary key and two text columns.

LANGUAGE: sql
CODE:
create table movies (
  id bigint generated by default as identity primary key,
  name text,
  description text
);

----------------------------------------

TITLE: Creating a SELECT Policy for Public Access
DESCRIPTION: This SQL snippet shows how to create a policy that allows public read access to a profiles table.

LANGUAGE: sql
CODE:
create table profiles (
  id uuid primary key,
  user_id references auth.users,
  avatar_url text
);

alter table profiles enable row level security;

create policy "Public profiles are visible to everyone."
on profiles for select
to anon
using ( true );

----------------------------------------

TITLE: Creating a Next.js app with Supabase integration
DESCRIPTION: Uses create-next-app command with the with-supabase template to set up a Next.js project pre-configured with Cookie-based Auth, TypeScript, and Tailwind CSS.

LANGUAGE: bash
CODE:
npx create-next-app -e with-supabase
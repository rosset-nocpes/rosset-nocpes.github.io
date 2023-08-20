<script lang="ts">
	import { fly } from 'svelte/transition';
	import { cubicOut, quintOut } from 'svelte/easing';
	import Button from './Button.svelte';

	export let tall = false;
	export let shrink = false;
	export let commission = false;
	export let img = '';
	export let subtitle = 'Click anywhere to dismiss';
	export let title = '';
	export let description = '';
	export let buttonText = '';
	export let href = '';

	let clicked = false;

	function onKeyDown(e: KeyboardEvent) {
		if (e.key === 'Escape') {
			clicked = false;
		}
	}
</script>

<button
	class="card"
	class:tall
	class:shrink
	style="background-image:url(art/{img})"
	aria-label={title}
	on:click={() => (clicked = true)}
	on:keypress={() => (clicked = true)}
/>

<svelte:window on:keydown={onKeyDown} />

<svelte:head>
	{#if clicked}
		<title>~r.s · {title}</title>
	{:else}
		<title>~r.s</title>
	{/if}
</svelte:head>

{#if clicked === true}
	<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
	<div
		class="img-modal"
		oncontextmenu={commission ? 'return false;' : ''}
		tabindex="0"
		on:click={() => (clicked = false)}
		on:keypress={() => (clicked = false)}
		in:fly={{ y: 50, easing: quintOut, duration: 750 }}
		out:fly={{ y: 50, easing: cubicOut, duration: 300 }}
	>
		<section>
			<!--<h3>{img}</h3>-->
			<img src="art/{img}" alt={title} />
			<div class="texted">
				<h2>{title}</h2>
				<h5>{description}</h5>
				<div class="margin-top-b">
					<a href={href} target="_blank">
						<Button>{buttonText}</Button>
					</a>
				</div>
				<h6>{subtitle}</h6>
			</div>
		</section>
	</div>
{/if}

<style lang="scss">
	.card {
		position: relative;
		border: none;
		padding: none;
		height: 100%;
		width: 100%;
		border-radius: 4px;
		overflow: hidden;
		background: var(--neutral-one);
		transition: all 0.3s var(--bezier-one);
		cursor: pointer;
		font-size: 0;
		user-select: none;
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		-webkit-transform: translate3d(0, 0, 1px);
		-webkit-backface-visibility: hidden;

		&:hover {
			transform: translateY(-1px);
			box-shadow: 0px 15px 25px -10px rgba(0, 0, 0, 0.25);
		}

		@media screen and (max-width: 868px) {
			border-radius: 0;
		}
	}

	.img-modal {
		background-blend-mode: overlay;
		display: flex;
		justify-content: center;
		align-items: center;
		position: fixed;
		text-align: center;
		left: 0;
		top: 50%;
		transform: translateY(-50%);
		height: 200vh;
		width: 100vw;
		z-index: 20;
		cursor: pointer;
		user-select: none;
		background-color: #0a0808bb;
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);

		img {
			max-height: 32vh;
			height: auto;
			max-width: 86vw;
			border-radius: 2vh;
			display: flex;
			justify-content: center;
			align-items: center;
		}
	}

	h3,
	h6 {
		margin-top: 1vh;
	}

	h6 {
		font-size: 2vh;
		margin-top: 2vh;
	}

	h3 {
		font-size: 3.5vh;
		font-weight: 500;
		color: var(--white);
		display: flex;
	}

	h2 {
		display: flex;
	}

	h5 {
		display: flex;
	}

	section {
		display: flex;
		align-items: center;
		justify-content: center;
		width: min(90%, 70rem) !important;
	}

	a {
		text-decoration: none;
	}

	.texted {
		display: flex;
		flex-direction: column;
		text-align: left;
		margin-left: 1rem;
	}

	.margin-top-b {
		margin-top: 2vh;
	}

	.tall {
		grid-row: span 2 / auto;
	}

	@media only screen and (max-width: 1153px) {
		.shrink {
			grid-row: span 1 / auto;
			background-position: top;
		}
	}

	@media screen and (max-width: 868px) {
		section {
			flex-direction: column;
		}
	}
</style>
